"""
1. Create + Inspect + Basic Cleaning
    Create a DataFrame from a dict (at least 10 rows).
    Show .head() , .info() , .describe(include="all") .
    Convert a date column to datetime.
    Trim whitespace from string columns

"""
import pandas as pd

data = {
    "date": [
        "2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05",
        "2026-03-06", "2026-03-07", "2026-03-08", "2026-03-09", "2026-03-10"
    ], 
    
    "category": [
        " Electronics ", "  Home   ", "   Electronics ", "  Beauty  ", " Home  ",
        " Beauty  ", "   Electronics   ", "   Grocery  ", "  Grocery  ",  "  Home  "
    ],
    
    "quantity": [5, 12, 8, 20, 15, 7, 3, 50, 45, 10]
}

df = pd.DataFrame(data)

print("\n--------------head--------------\n")
print(df.head())

print("\n--------------info--------------\n")
print(df.info())

print("\n--------------describe--------------\n")

print(df.describe(include="all"))

# converting column to datetime
df["date"] = pd.to_datetime(df["date"])

print("\nAfter converting date column to datetime: df['date'].dtype = ", df["date"].dtype)

# trimming white spaces from category column
columns = df.select_dtypes(include = "object").columns

df[columns] = df[columns].apply(lambda x: x.str.strip())
print("\nAfter trimming white spaces:\n", df.head())