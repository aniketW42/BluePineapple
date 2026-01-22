"""
Window Functions (Intermediate)
    For each customer:
        sort by order_date
        compute prev_order_date
        compute days_since_prev
        compute rolling 3-order average net_amount
    Identify customers whose average order value is increasing (simple
    heuristic).

"""
import pandas as pd

df = pd.read_csv("..\\datasets\\orders.csv")

# sort by order_date
df["order_date"] = pd.to_datetime(df["order_date"])
df = df.sort_values("order_date")

#compute prev_order_date
df["prev_order_date"] = df.groupby("customer_id")["order_date"].shift(1)

#compute days_since_prev
df["days_since_prev"] = df["order_date"] - df["prev_order_date"]

#rolling 3-order average net_amount
df["3D_rolling_avg"] = (df.groupby("customer_id")["net_amount"].
                        transform(lambda x: x.rolling(window=3, min_periods=1)
                        .mean()))

# finding first and last rolling averate of each customer
trend = df.groupby("customer_id")["3D_rolling_avg"].agg(first_avg="first",  last_avg= "last")

# computing if it is increasing or not
trend["is_increasing"] = trend["first_avg"] < trend["last_avg"] 

# customers whose average order value is increasing
increasing_avg_customer = trend[trend["is_increasing"]==True]
print(increasing_avg_customer)