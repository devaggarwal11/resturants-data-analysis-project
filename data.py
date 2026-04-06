import pandas as pd

# CSV file load
df = pd.read_csv("skycity_data.csv")

# first 5 rows print
# print(df.head())

# print(df["MonthlyOrders"].sum())
channel_totals = {
    'InStore': df['InStoreOrders'].sum(),
    'UberEats': df['UberEatsOrders'].sum(),
    'DoorDash': df['DoorDashOrders'].sum(),
    'SelfDelivery': df['SelfDeliveryOrders'].sum()
}

print(channel_totals)

total_orders = df['MonthlyOrders'].sum()

channel_totals_percent = {k: (v / total_orders) * 100 for k, v in channel_totals.items()}

print(channel_totals_percent)


subregion_analysis = df.groupby('Subregion')[[
    'InStoreOrders',
    'UberEatsOrders',
    'DoorDashOrders',
    'SelfDeliveryOrders'
]].sum()

print(subregion_analysis)

cuisine_analysis = df.groupby('CuisineType')[[
    'InStoreOrders',
    'UberEatsOrders',
    'DoorDashOrders',
    'SelfDeliveryOrders'
]].mean()

print(cuisine_analysis["SelfDeliveryOrders"].sort_values(ascending=False))

df['Max_Channel_Share'] = df[['InStoreShare', 'UE_share', 'DD_share', 'SD_share']].max(axis=1)

risky = df[df['Max_Channel_Share'] > 0.7]

print(risky[['RestaurantName', 'Max_Channel_Share']])






