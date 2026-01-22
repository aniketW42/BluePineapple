"""
4. GroupBy Aggregations
    Group by city and compute:
        total orders
        unique customers
        total revenue (sum net_amount)
        average order value
    Sort by revenue desc and show top 10 

"""

import pandas as pd

df = pd.read_csv("..\\datasets\\orders.csv")

city_info = df.groupby("city").agg(
    total_orders = ("order_id", "count"),
    unique_customers = ("customer_id", "nunique"),
    total_revenue = ("net_amount", "sum"),
    average_order_value = ("net_amount", "mean")
)

print(city_info, end="\n\n")

sorted_city_info = city_info.sort_values("total_revenue", ascending=False)

print(sorted_city_info)