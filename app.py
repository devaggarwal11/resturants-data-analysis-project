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