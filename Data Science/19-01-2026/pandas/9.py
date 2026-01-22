"""
Outlier Detection + Capping (Intermediate)
    For each category:
        compute IQR of net_amount
        flag outliers (outside [Q1-1.5IQR, Q3+1.5IQR])
        cap outliers to bounds (winsorize)
    Report outlier counts by category before/after.

"""

import pandas as pd 
import numpy as np

df = pd.read_csv("..\\datasets\\orders.csv")

def process_outlier(group):

    Q1 = group["net_amount"].quantile(0.25)
    Q3 = group["net_amount"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5*IQR
    upper_bound = Q3 + 1.5*IQR

    group['is_outlier'] = (group['net_amount'] < lower_bound) | (group['net_amount'] > upper_bound)

    group['net_amount_capped'] = group['net_amount'].clip(lower=lower_bound, upper=upper_bound)
    
    print(group)

    return group

df = df.groupby("category", group_keys=False).apply(process_outlier)

# print(df)

report = df.groupby('category').agg(
    total_rows=('net_amount', 'count'),
    outlier_count=('is_outlier', 'sum')
).reset_index()

# print(report)