import numpy as np
np.random.seed(42)

#---------------- Part A: Array Creation & Exploration-------------------

# 1. Temperature Data: 365 days × 5 cities
temperatures = np.random.uniform(-10.0, 40.0, (365, 5))

print("Temperature Data (first 5 days):")
print(temperatures[:5])

print("\n--- Temperature Array Info ---")
print("Shape:", temperatures.shape)
print("Dimensions:", temperatures.ndim)
print("Data type:", temperatures.dtype)
print("Size:", temperatures.size)

# 2. Sales Matrix: 12 months × 4 product categories
sales = np.random.randint(1000, 5001, (12, 4))
print("\nSales Matrix (12×4):")
print(sales)

print("\n--- Sales Array Info ---")
print("Shape:", sales.shape)
print("Dimensions:", sales.ndim)
print("Data type:", sales.dtype)
print("Size:", sales.size)

# 3. Special Arrays
identity_matrix = np.eye(5)
evenly_spaced = np.linspace(0, 100, 50)
print("\nIdentity Matrix (5x5):\n", identity_matrix)
print("\n50 evenly spaced values from 0 to 100:\n", evenly_spaced)


# -----------------Part B: Array Manipulation & Indexing-----------------

# Basic Slicing
january_data = temperatures[:31, :]
summer_data = temperatures[152:244, :]
weekend_data = temperatures[4::7, :]

# Boolean Indexing
hot_days_mask = (temperatures > 35).any(axis=1)
hot_days_indices = np.where(hot_days_mask)[0]
freezing_days_count = (temperatures < 0).sum(axis=0)
comfortable_days_mask = (temperatures >= 15) & (temperatures <= 25)

# Data cleaning: replace temperatures < -5°C with -5
np.maximum(temperatures, -5, out=temperatures)

# Fancy Indexing
specific_days_data = temperatures[[0, 100, 200, 300, 364], :]
quarters = np.array_split(temperatures, 4)
quarterly_avg = np.array([q.mean(axis=0) for q in quarters])

# Rearrange cities by annual average temperature (descending)
annual_avg_per_city = temperatures.mean(axis=0)
sorted_indices = np.argsort(annual_avg_per_city)[::-1]
sorted_temperatures = temperatures[:, sorted_indices]


#  ----------------------Part C: Mathematical Operations & Statistics---------------

# Temperature Analysis
mean_per_city = temperatures.mean(axis=0)
median_per_city = np.median(temperatures, axis=0)
std_per_city = np.std(temperatures, axis=0)
temp_range_per_city = temperatures.max(axis=0) - temperatures.min(axis=0)
correlation_matrix = np.corrcoef(temperatures, rowvar=False)

daily_avg = temperatures.mean(axis=1)
hottest_day_index = np.argmax(daily_avg)
coldest_day_index = np.argmin(daily_avg)

# Sales Analysis
total_sales_per_category = sales.sum(axis=0)
avg_sales_per_category = sales.mean(axis=0)
best_month_index = np.argmax(sales.sum(axis=1))
best_category_index = np.argmax(total_sales_per_category)

# Advanced Computations
window_size = 7
moving_avg = np.apply_along_axis(
    lambda m: np.convolve(m, np.ones(window_size)/window_size, mode='valid'),
    axis=0,
    arr=temperatures
)

z_scores = (temperatures - mean_per_city) / std_per_city
percentiles = np.percentile(temperatures, [25, 50, 75], axis=0)



# Display Results
print("\n=== Temperature Statistics per City ===")
for i in range(5):
    print(f"City {i+1}: Mean={mean_per_city[i]:.2f}, Median={median_per_city[i]:.2f}, Std={std_per_city[i]:.2f}, Range={temp_range_per_city[i]:.2f}")

print(f"\nHottest Day (avg across cities): Day {hottest_day_index+1}, Temp={daily_avg[hottest_day_index]:.2f}°C")
print(f"Coldest Day (avg across cities): Day {coldest_day_index+1}, Temp={daily_avg[coldest_day_index]:.2f}°C")

print("\n=== Correlation Between Cities ===")
print(correlation_matrix)

print("\n=== Sales Analysis ===")
for i, (total, avg) in enumerate(zip(total_sales_per_category, avg_sales_per_category), 1):
    print(f"Category {i}: Total Sales={total}, Avg Monthly={avg:.2f}")
print(f"Best Month Overall: Month {best_month_index+1} with total sales={sales[best_month_index].sum()}")
print(f"Best Category Overall: Category {best_category_index+1} with total sales={total_sales_per_category[best_category_index]}")

print("\n7-Day Moving Average Shape:", moving_avg.shape)
print("Z-Scores Shape:", z_scores.shape)

print("\nPercentiles per City (25th, 50th, 75th):")
for i in range(5):
    print(f"City {i+1}: 25th={percentiles[0,i]:.2f}, 50th={percentiles[1,i]:.2f}, 75th={percentiles[2,i]:.2f}")
