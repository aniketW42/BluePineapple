"""
Cohort Analysis (Intermediate)
    Define cohort month = customer's first order month.
    For each cohort, compute:
        number of active customers by month offset (M0, M1, M2…)
        retention rate matrix (cohort table)
    Output as a DataFrame shaped like a retention heatmap table (values as
    %).

"""
import pandas as pd


df = pd.read_csv("..\\datasets\\orders.csv")

df['order_date']  = pd.to_datetime(df['order_date'])

df['order_month'] = df['order_date'].dt.to_period('M')

# Define cohort month = customer's first order month.

df['cohort_month'] = df.groupby('customer_id')['order_month'].transform('min')

# number of active customers by month offset

df['offset'] = (df['order_month'] - df['cohort_month']).apply(lambda x: x.n)

cohort_counts = df.groupby(['cohort_month', 'offset'])['customer_id'].nunique()
cohort_counts = cohort_counts.reset_index()

retention_matrix = cohort_counts.pivot(index='cohort_month', columns='offset', values='customer_id')

cohort_size = retention_matrix.iloc[:, 0]

retention_rate = retention_matrix.divide(cohort_size, axis=0).round(4) * 100

# retention rate matrix

print(retention_rate)
