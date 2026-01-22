"""
Joins / Merges (Customers + Orders)
    Create a customers DataFrame: customer_id , signup_date , segment .
        Merge with orders.
    Compute revenue by segment and retention proxy:
    “active in last 60 days” per segment.
"""

import pandas as pd

df_customers = pd.read_csv("..\\datasets\\customers.csv")
df_orders = pd.read_csv("..\\datasets\\orders.csv")

df = pd.merge(df_customers, df_orders, on='customer_id', how='inner')

df["order_date"] = pd.to_datetime(df["order_date"])

max_date = df["order_date"].max()

cutoff_date = max_date - pd.Timedelta(days=60)

active_in_last_60_days = df[df["order_date"] > cutoff_date]

print(active_in_last_60_days.groupby(["segment"]).agg(revenue = ("net_amount", "sum"), active_customer_count=("customer_id", "nunique")))
# print(customers_orders_df)