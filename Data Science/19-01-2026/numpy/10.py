"""
Time Series Rolling Window Stats
    Create a 1D array representing 365 days of random “daily sales”.
    Python for Data Science - Assignments 3
    Compute rolling 7-day mean and rolling 30-day mean using NumPy (no pandas).
    Detect days where sales are > (rolling_30_mean + 2*rolling_30_std).

"""
import numpy as np

np.random.seed(42)
sales = np.random.randint(100, 1000, size=365).astype(float)


def get_rolling_stats(data, window):
    windows = np.lib.stride_tricks.sliding_window_view(data, window)
    
    means = np.full(data.shape, np.nan)
    stds = np.full(data.shape, np.nan)
    
    means[window-1:] = windows.mean(axis=-1)
    stds[window-1:] = windows.std(axis=-1)
    
    return means, stds


# Manually set massive value
sales[50] = 5000 
sales[60] = 600000

mean_30, std_30 = get_rolling_stats(sales, 30)
threshold = mean_30 + (2 * std_30)
outliers_mask = sales > threshold
print(f"Spikes detected on days: {np.where(outliers_mask)[0]}")
