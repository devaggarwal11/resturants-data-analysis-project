import streamlit as st

st.title("Restaurant Channel Analysis")

st.write(df.head())

sub = st.selectbox("Select Subregion", df['Subregion'].unique())

filtered = df[df['Subregion'] == sub]

st.bar_chart(filtered[['InStoreOrders','UberEatsOrders']])


df['Total_Share'] = df['InStoreShare'] + df['UE_share'] + df['DD_share'] + df['SD_share']

df.isnull()