"""
9. Linear Regression From Scratch
    Generate synthetic data:
        X: 200 samples, 1 feature (random)
        y = 3*X + 5 + noise
    Fit using closed-form normal equation (no sklearn).
    Print estimated slope and intercept.

"""
import numpy as np

# Generate synthetic data
np.random.seed(42)

X_raw = 2 * np.random.rand(200, 1) 

print(X_raw)

noise = np.random.randn(200, 1)
y = 3 * X_raw + 5 + noise           # y = 3*X + 5 + noise

# Prepare Feature Matrix
X_b = np.c_[np.ones((200, 1)), X_raw]

# Fit using Normal Equation -> theta = inv(X_T * X) * X_T * y
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# 4. Print results
intercept, slope = theta[0][0], theta[1][0]
print(f"Estimated Intercept: {intercept:.4f}")
print(f"Estimated Slope: {slope:.4f}")

