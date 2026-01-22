"""
Handling Missing Values
    Randomly introduce missing values in city, payment_mode, and discount_pct.
    Apply different strategies:
        fill categorical with “Unknown”
        fill numeric with median by category
    Prove it worked: show missing counts before/after.

"""

import pandas as pd 
import numpy as np
df = pd.read_csv("..\\datasets\\orders.csv")

# random missing values
df.loc[df.sample(frac = 0.2).index, "city"] = np.nan
df.loc[df.sample(frac = 0.3).index, "payment_mode"] = np.nan
df.loc[df.sample(frac = 0.4).index, "discount_pct"] = np.nan


missing_count_before = df.isna().sum()

# fill categorical with “Unknown”
categorical_columns = df.select_dtypes(include = ["object"]).columns
df[categorical_columns] = df[categorical_columns].fillna("Unknown")

# fill numeric with median by category
df["discount_pct"] = df.groupby("category")["discount_pct"].transform(lambda x: x.fillna(x.median()))

print("missing count before:\n", missing_count_before)
print("\nmissing count after:\n", df.isna().sum())
