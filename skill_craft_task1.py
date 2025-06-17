

#Histogram

import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Simulate 1,000,000 sample individuals based on age distribution
group_0_20 = np.random.randint(0, 21, int(0.361 * 1_000_000))     # Yellow
group_21_64 = np.random.randint(21, 65, int(0.57 * 1_000_000))    # Blue
group_65_plus = np.random.randint(65, 101, int(0.069 * 1_000_000))# Pink

# Plot overlapping histograms
plt.figure(figsize=(10, 6))
plt.hist(group_0_20, bins=20, alpha=0.7, color='gold', label='0-20 Years')
plt.hist(group_21_64, bins=20, alpha=0.7, color='deepskyblue', label='21-64 Years')
plt.hist(group_65_plus, bins=20, alpha=0.7, color='hotpink', label='65+ Years')

# Add labels and grid
plt.title("India's Simulated Age Distribution (2022)", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Population Count (sampled)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save output (optional)
plt.savefig("age_histogram_output.png", dpi=300)
plt.show()
