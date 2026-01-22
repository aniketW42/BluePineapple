"""
Filtering + Multi-condition Queries
    Filter orders:
        category in a set (e.g., Electronics/Fashion)
        net_amount > X
        order_date within last N days (relative to max date )
    Output count + total net_amount .

"""
import pandas as pd

df = pd.read_csv("..\\datasets\\orders.csv")

print("Dataframe:\n", df.head())

# filter by categories
filter_categories = ["Electronics", "Fashion"]
electronics_or_fashion = df[df["category"].isin(filter_categories)]
print("\nFilterd by categoris (Electronics/Fashion):\n", electronics_or_fashion)

# net_amount > X
X = 10000
net_amount_gt_50000 = df[df["net_amount"] > X]
print("\nFiltered rows with net-amount>50000:\n", net_amount_gt_50000)

#order_date within last N days 
N = 30
df["order_date"] = pd.to_datetime(df["order_date"])
max_date = df["order_date"].max()
Nth_date = max_date - pd.Timedelta(N, unit='D') 
data_with_orderdate_within_last_N_days = df[df["order_date"] > Nth_date]

print("\nData with order date within last 40 days\n",data_with_orderdate_within_last_N_days)

# Output count + total net_amount 
print("Count :", data_with_orderdate_within_last_N_days.shape[0])
print("Total net amount:", data_with_orderdate_within_last_N_days["net_amount"].sum())  