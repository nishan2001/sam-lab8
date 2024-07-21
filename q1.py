import numpy as np

# Example data (replace with your actual data)
sample_data = np.array([22, 18, 25, 30, 28, 24, 26, 29, 31, 27])
population_mean = 25  # Replace with your known population mean

# Calculate sample mean
sample_mean = np.mean(sample_data)

# Calculate bias
bias = sample_mean - population_mean

# Print results
print(f"Sample Mean (Point Estimation): {sample_mean}")
print(f"Bias: {bias}")
