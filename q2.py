import numpy as np
from scipy import stats

# Example data (replace with your actual data)
sample_data = np.array([22, 18, 25, 30, 28, 24, 26, 29, 31, 27])
population_mean = 25  # Replace with your known population mean

# Calculate sample statistics
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # ddof=1 for sample standard deviation
n = len(sample_data)

# Choose confidence level and determine critical value
confidence_level = 0.95  # 95% confidence interval
alpha = 1 - confidence_level
degrees_freedom = n - 1
t_critical = stats.t.ppf(1 - alpha/2, degrees_freedom)  # Two-tailed t-score

# Calculate margin of error
margin_of_error = t_critical * (sample_std / np.sqrt(n))

# Calculate confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Print results
print(f"Sample Mean: {sample_mean}")
print(f"Sample Standard Deviation: {sample_std}")
print(f"Confidence Interval ({confidence_level*100}%): ({lower_bound}, {upper_bound})")
