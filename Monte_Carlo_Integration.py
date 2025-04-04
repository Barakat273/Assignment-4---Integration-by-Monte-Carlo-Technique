import numpy as np

# Function to integrate
def f(x):
    return np.exp(-x ** 2 / 2)
# Monte Carlo Integration
def monte_carlo_integration(a, b, N):
    # Generate N random points in [a, b]
    x_random = np.random.uniform(a, b, N)

    # Compute function values at random points
    value = f(x_random)
    # Estimate the integral
    integral = (b - a) * np.mean(value)

    return integral
# Define limits
a = 1  # You can set any value for 'a'
b = 20  # Given in the problem
N = 100000  # Number of random samples

# Compute and print the result
result = monte_carlo_integration(a, b, N)
print(f"Integral value: {result}")

