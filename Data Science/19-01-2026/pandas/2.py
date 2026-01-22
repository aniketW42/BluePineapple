"""
2. Add Derived Columns
    Using quantity , unit_price , discount_pct :
        compute gross_amount = quantity * unit_price
        compute net_amount = gross_amount * (1 - discount_pct/100)
    Add a is_high_value flag ( net_amount > threshold ).

"""

import pandas as pd 

df = pd.read_csv("..\\datasets\\orders.csv")

print("Dataframe:\n", df.head())

df["gross_amount"] = df["quantity"] * df["unit_price"]

print("\nAdded gross amount:\n", df.head())

df["net_amount"] = df["gross_amount"] * (1 - df["discount_pct"]/100)

print("\nAdded net_ammount:\n",df.head())

df["is_high_value"] = df["net_amount"] > 50000

print("\nAdded is_high_value (True if net_amount > 50000):\n", df.head())


df.to_csv("..\\datasets\\orders.csv")