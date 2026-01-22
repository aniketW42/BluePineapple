"""
Pivot Table Dashboard View
    Create a pivot:
        index: month (from order_date )
        columns: category
        values: net_amount sum
    Add a “Grand Total” column and compute month-over-month growth %.

"""

import pandas as pd


df = pd.read_csv("..\\datasets\\orders.csv")

index_month = pd.to_datetime(df["order_date"]).dt.to_period("M")

pivot = df.pivot_table(
    index = index_month,
    columns = "category",
    values = "net_amount",
    aggfunc = "sum"
)

pivot["Grand Total"] = pivot.sum(axis=1)
pivot["Percentage Change"] = pivot["Grand Total"].pct_change()*100
print(pivot)