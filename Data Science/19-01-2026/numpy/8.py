"""
8. Missing Values Simulation
    Create a 1D float array of size 40.
    Randomly turn 20% positions into np.nan.
    Compute mean ignoring NaNs.
    Replace NaNs with the median of non-NaN values.

"""
import numpy as np

# Create a 1D float array of size 40.
float_arr = np.random.rand(40)

# generating random 20% positions
random_idx = np.random.choice(40, size=8, replace=False)

# turning them into np.nan
float_arr[random_idx] = np.nan

# mean ignoring nans
mean_val = np.nanmean(float_arr)

# replacing the nan values with median
median_val = np.nanmedian(float_arr)

mask = np.isnan(float_arr)
float_arr[mask] = median_val


print(float_arr)
