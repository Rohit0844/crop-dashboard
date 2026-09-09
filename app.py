import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Seasonal Agriculture Analytics', layout='wide')
st.title('🌾 Seasonal Agriculture Performance Analytics')
st.caption('VOIS AICTE Major Project — interactive decision dashboard')

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
for c in ['Rainfall_mm','Soil_Moisture_pct','Yield_Tonnes_Ha']:
    df[c] = df[c].fillna(df[c].median())

season_order = ['Kharif','Rabi','Zaid']
season = df.groupby('Season').agg(
    Farms=('Farm_ID','count'),
    Yield=('Yield_Tonnes_Ha','mean'),
    Revenue=('Revenue_INR','mean'),
    Cost=('Total_Cost_INR','mean'),
    Profit=('Profit_INR','mean'),
    Water=('Water_Used_m3','mean'),
    Efficiency=('Water_Efficiency_t_per_1000m3','mean'),
    Risk=('Disease_Pest_Risk_pct','mean')
).reindex(season_order)
season['Margin'] = season['Profit']/season['Revenue']*100

c1,c2,c3,c4 = st.columns(4)
c1.metric('Farms', f'{len(df):,}')
c2.metric('Avg Yield', f"{df.Yield_Tonnes_Ha.mean():.2f} t/ha")
best = season.Profit.idxmax()
c3.metric('Best Avg Profit Season', best)
c4.metric('Best Avg Margin', f"{season.Margin.max():.1f}%")

st.subheader('Seasonal performance')
st.dataframe(season.round(2), use_container_width=True)

fig, ax = plt.subplots(figsize=(8,4))
season[['Yield','Profit']].plot(kind='bar', ax=ax)
ax.set_title('Yield and Profit by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Average value')
plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig)

st.subheader('Crop-season profitability')
cs = df.groupby(['Season','Crop']).agg(
    Yield=('Yield_Tonnes_Ha','mean'),
    Revenue=('Revenue_INR','mean'),
    Cost=('Total_Cost_INR','mean'),
    Profit=('Profit_INR','mean')
).reset_index()
cs['Margin %'] = cs.Profit/cs.Revenue*100
st.dataframe(cs.sort_values('Margin %', ascending=False).round(2), use_container_width=True)

st.subheader('Explore')
selected = st.multiselect('Select seasons', season_order, default=season_order)
view = df[df.Season.isin(selected)]
st.write(f'Rows shown: {len(view):,}')
st.dataframe(view.head(100), use_container_width=True)
