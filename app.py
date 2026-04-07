import streamlit as st
import pandas as pd

# CSV file load
df = pd.read_csv("skycity_data.csv")

st.title("Restaurant Channel Analysis")

st.write(df.head())

sub = st.selectbox("Select Subregion", df['Subregion'].unique())

filtered = df[df['Subregion'] == sub]

st.bar_chart(filtered[['InStoreOrders','UberEatsOrders']])


df['Total_Share'] = df['InStoreShare'] + df['UE_share'] + df['DD_share'] + df['SD_share']

df.isnull()

st.write(df.columns)
st.metric("Total Orders", df['MonthlyOrders'].sum())


import pandas as pd
import streamlit as st
import plotly.express as px

# Page config
st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("skycity_data.csv")

# Title
st.title("📊 Restaurant Channel Analysis Dashboard")

#  KPI CARDS
col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", int(df['MonthlyOrders'].sum()))
col2.metric("Avg AOV", round(df['AOV'].mean(), 2))
col3.metric("Growth Factor", round(df['GrowthFactor'].mean(), 2))

# 🎛️ Sidebar filter
st.sidebar.header("Filters")
sub = st.sidebar.selectbox("Select Subregion", df['Subregion'].unique())

# Filter data
filtered = df[df['Subregion'] == sub]

# 📊 Chart (upgrade from bar_chart)
fig = px.bar(
    filtered,
    x="RestaurantName",
    y=["InStoreOrders", "UberEatsOrders"],
    barmode="group",
    title="Orders by Channel"
)

st.plotly_chart(fig, use_container_width=True)

# 📋 Table
st.subheader("📋 Data Preview")
st.dataframe(filtered, use_container_width=True)

#  Insights
st.subheader(" Insights")

st.write(f"""
- Selected Region: **{sub}**
- Total Orders: **{int(filtered['MonthlyOrders'].sum())}**
- Highest AOV: **{round(filtered['AOV'].max(),2)}**
""")

st.download_button("Download Data", filtered.to_csv(), "data.csv")

top = filtered.sort_values(by='MonthlyOrders', ascending=False).iloc[0]
st.write(f" Top Restaurant: {top['RestaurantName']}")

cuisine = st.sidebar.selectbox("Cuisine", df['CuisineType'].unique())
segment = st.sidebar.selectbox("Segment", df['Segment'].unique())

filtered = df[
    (df['Subregion'] == sub) &
    (df['CuisineType'] == cuisine) &
    (df['Segment'] == segment)
]


fig = px.line(filtered, x="RestaurantID", y="MonthlyOrders", title="Order Trend")
st.plotly_chart(fig)


fig = px.bar(filtered, 
             x="RestaurantName", 
             y=["InStoreOrders","UberEatsOrders"],
             barmode="group",
             title="Channel Comparison")

st.plotly_chart(fig)


st.metric("Total Orders", 
          int(filtered['MonthlyOrders'].sum()),
          delta="+5%")
from sklearn.linear_model import LinearRegression

X = df[['AOV']]
y = df['MonthlyOrders']

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[50]])
st.write(f"Predicted Orders for AOV 50: {int(pred[0])}")

st.download_button("Download CSV", filtered.to_csv(), "report.csv")


st.subheader(" Smart Insights")

top = filtered.sort_values(by='MonthlyOrders', ascending=False).iloc[0]

st.write(f"""
- Top restaurant: **{top['RestaurantName']}**
- Highest orders: **{top['MonthlyOrders']}**
- Most popular channel: **InStore**
""")

st.markdown("---")

st.subheader(" Restaurant Locations")



import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📊 Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)

st.pyplot(fig)