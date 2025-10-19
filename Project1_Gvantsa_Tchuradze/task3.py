# improved_analysis.py
import numpy as np
from typing import Tuple, Dict

np.random.seed(42)

# Constants / Indices
N_USERS, N_DAYS, N_METRICS = 100, 90, 4
STEPS, CALS, AMINS, HR = 0, 1, 2, 3


#---------------- Part A: Data Generation & Preparation--------------------
def generate_data(seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """Generate realistic synthetic data and metadata according to specification."""
    np.random.seed(seed)

    # Steps: lognormal centered near 8000, clipped to [2000, 15000]
    steps = np.random.lognormal(mean=np.log(8000), sigma=0.35, size=(N_USERS, N_DAYS))
    steps = np.clip(steps, 2000, 15000).round().astype(int)

    # Calories: baseline 1500 plus an approx linear relationship with steps + gaussian noise
    # scale chosen so steps variation maps to ~0-2000 cal range; then clip to [1500,3500]
    calories = 1500 + (steps - 2000) * (2000 / (15000 - 2000)) + np.random.normal(0, 200, (N_USERS, N_DAYS))
    calories = np.clip(calories.round().astype(int), 1500, 3500)

    # Active minutes: normal around 75, sd 25, clip to [20,180]
    active_minutes = np.clip(np.random.normal(75, 25, (N_USERS, N_DAYS)).round().astype(int), 20, 180)

    # Avg heart rate: normal around 85, sd 12, clip to [60,120]
    avg_hr = np.clip(np.random.normal(85, 12, (N_USERS, N_DAYS)).round().astype(int), 60, 120)

    # Stack into shape (users, days, metrics) as float to permit NaNs
    data = np.stack([steps, calories, active_minutes, avg_hr], axis=2).astype(float)

    # Metadata: user_id (1..100), age (18-70), gender (0/1)
    user_ids = np.arange(1, N_USERS + 1)
    ages = np.random.randint(18, 71, size=N_USERS)   # 18..70 inclusive
    genders = np.random.randint(0, 2, size=N_USERS) # 0/1
    metadata = np.stack([user_ids, ages, genders], axis=1)

    return data, metadata

def introduce_issues(data: np.ndarray, nan_frac: float = 0.05, outlier_frac: float = 0.02) -> np.ndarray:
    """Introduce NaNs and extreme outliers to mimic equipment failure and unrealistic readings."""
    corrupted = data.copy()
    total_positions = corrupted.size
    n_nan = int(nan_frac * total_positions)
    flat = corrupted.reshape(-1)
    nan_idx = np.random.choice(flat.size, size=n_nan, replace=False)
    flat[nan_idx] = np.nan
    corrupted = flat.reshape(N_USERS, N_DAYS, N_METRICS)

    # Define extreme unrealistic values per metric (lower and upper extremes)
    extremes = np.array([
        [0, 50000],    # steps
        [300, 12000],  # calories
        [0, 720],      # active minutes
        [0, 240],      # heart rate
    ], dtype=float)

    # For each metric, pick outlier_frac of VALID entries and set to extremes
    for k in range(N_METRICS):
        arr = corrupted[:, :, k].reshape(-1)
        valid_idx = np.where(~np.isnan(arr))[0]
        n_out = max(1, int(outlier_frac * valid_idx.size))
        chosen = np.random.choice(valid_idx, n_out, replace=False)
        half = n_out // 2
        arr[chosen[:half]] = extremes[k, 0]
        arr[chosen[half:]] = extremes[k, 1]
        corrupted[:, :, k] = arr.reshape(N_USERS, N_DAYS)

    return corrupted

# generate and corrupt
raw_data, metadata = generate_data(seed=42)
data = introduce_issues(raw_data, nan_frac=0.05, outlier_frac=0.02)

# -----------------------Part B: Data Cleaning & Validation--------------------------
def handle_missing(data_3d: np.ndarray) -> np.ndarray:
    """Replace NaN with per-metric mean (computed ignoring NaNs)."""
    cleaned = data_3d.copy()
    # compute mean per metric across users*days
    for k in range(cleaned.shape[2]):
        metric = cleaned[:, :, k]
        mean_val = np.nanmean(metric)
        metric[np.isnan(metric)] = mean_val
        cleaned[:, :, k] = metric
    return cleaned

def remove_outliers_iqr(data_3d: np.ndarray, metric_idx: int) -> np.ndarray:
    """
    Replace outliers for metric metric_idx (IQR method) with median (ignoring NaNs).
    Operates only on the specified metric (vectorized).
    """
    cleaned = data_3d.copy()
    metric = cleaned[:, :, metric_idx]

    # flatten and compute percentiles ignoring NaN
    q1, q3 = np.nanpercentile(metric, [25, 75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    median = np.nanmedian(metric)
    mask = (metric < lower) | (metric > upper)
    # Replace outliers with median
    metric[mask] = median
    cleaned[:, :, metric_idx] = metric
    return cleaned

def cleaning_pipeline(data_3d: np.ndarray) -> np.ndarray:
    """Apply outlier removal (per metric) then missing-value handling."""
    cleaned = data_3d.copy()
    for k in range(N_METRICS):
        cleaned = remove_outliers_iqr(cleaned, k)
    cleaned = handle_missing(cleaned)
    # final assertion: no NaNs remain
    assert not np.isnan(cleaned).any(), "NaNs remain after cleaning!"
    return cleaned

clean = cleaning_pipeline(data)

# ------------------------Part C: Comprehensive Analysis------------------

def per_user_stats(cleaned: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Return per-user mean and std arrays (shape (N_USERS, N_METRICS))."""
    user_means = cleaned.mean(axis=1)
    user_stds = cleaned.std(axis=1)
    return user_means, user_stds

user_means, user_stds = per_user_stats(clean)

# Top 10 active users (combined z across metrics)
mean_metric = user_means.mean(axis=0)
std_metric = user_means.std(axis=0)
std_metric_safe = np.where(std_metric == 0, 1, std_metric)
user_z = (user_means - mean_metric) / std_metric_safe
combined_z = user_z.sum(axis=1)
user_ids = metadata[:, 0].astype(int)
top10_users = user_ids[np.argsort(combined_z)[::-1][:10]]

# Most consistent users (lowest mean std across metrics)
consistency_score = user_stds.mean(axis=1)
most_consistent_users = user_ids[np.argsort(consistency_score)[:10]]

# Activity levels by steps percentiles
steps_avg = user_means[:, STEPS]
p25, p75 = np.percentile(steps_avg, [25, 75])
levels = np.empty(N_USERS, dtype=int)
levels[steps_avg < p25] = 0
levels[(steps_avg >= p25) & (steps_avg <= p75)] = 1
levels[steps_avg > p75] = 2

# Temporal trends: daily population-wide means (shape (days, metrics))
daily_means = clean.mean(axis=0)

# 7-day rolling mean (valid only where window fits)
rolling7 = np.vstack([
    np.convolve(daily_means[:, k], np.ones(7) / 7, mode='valid')
    for k in range(N_METRICS)
]).T  # shape: (N_DAYS-6, N_METRICS)

# Weekly pattern: day-of-week averages (0..6 -> Mon..Sun relative)
dow = np.arange(N_DAYS) % 7
weekly_means = np.array([clean[:, dow == i, :].mean(axis=(0, 1)) for i in range(7)])

# Trend detection over time per metric: linear fit slope (positive -> increasing)
days_idx = np.arange(N_DAYS)
trend_slopes = np.polyfit(days_idx, daily_means[:, 0], 1)[0], \
               np.polyfit(days_idx, daily_means[:, 1], 1)[0], \
               np.polyfit(days_idx, daily_means[:, 2], 1)[0], \
               np.polyfit(days_idx, daily_means[:, 3], 1)[0]

# Month-over-month growth: treat 90 days as three 30-day windows
def month_over_month(daily: np.ndarray) -> np.ndarray:
    months = 3
    msize = N_DAYS // months
    month_means = np.array([daily[i * msize:(i + 1) * msize, :].mean(axis=0) for i in range(months)])
    # growth rates between consecutive months (pct): (m2 - m1)/m1
    growth = (month_means[1:] - month_means[:-1]) / np.where(month_means[:-1] == 0, 1, month_means[:-1])
    return month_means, growth

month_means, mom_growth = month_over_month(daily_means)

# Correlations
flat = clean.reshape(-1, N_METRICS)
corr_matrix = np.corrcoef(flat, rowvar=False)

# Age vs activity (steps)
ages = metadata[:, 1].astype(float)
age_steps_corr = np.corrcoef(ages, steps_avg)[0, 1]

# Gender comparison (0 male, 1 female)
genders = metadata[:, 2].astype(int)
avg_steps_male = steps_avg[genders == 0].mean()
avg_steps_female = steps_avg[genders == 1].mean()

# Health score: weighted z-sum (weights sum not required to be 1)
weights = np.array([0.4, 0.2, 0.35, 0.05])
health_z = (user_means - mean_metric) / std_metric_safe
health_score = (health_z * weights).sum(axis=1)
health_top10_users = user_ids[np.argsort(health_score)[::-1][:10]]

# Goal achievement
goals = np.array([8000, 2000, 60])  # steps, calories, active minutes
met_steps = (clean[:, :, STEPS] >= goals[0])
met_cals = (clean[:, :, CALS] >= goals[1])
met_minutes = (clean[:, :, AMINS] >= goals[2])
all_goals_met = met_steps & met_cals & met_minutes
goal_achievement_rate = all_goals_met.mean(axis=1)  # fraction of days each user met all 3 goals
consistent_achievers = user_ids[goal_achievement_rate >= 0.8]

# -----------------------------
# Part D: Output (console + markdown)
# -----------------------------
# Console summary
print("=== SHAPES ===")
print("Raw data:", raw_data.shape, "Corrupted data:", data.shape, "Clean data:", clean.shape)
print("Metadata:", metadata.shape)

print("\n=== USER ACTIVITY ===")
print("Top 10 active users (combined z-score):", top10_users.tolist())
print("Most consistent users:", most_consistent_users.tolist())
print("Activity levels (Low/Med/High):", (levels == 0).sum(), (levels == 1).sum(), (levels == 2).sum())

print("\n=== TEMPORAL TRENDS ===")
print("7-day rolling mean shape:", rolling7.shape)
print("Weekly means by day of week:\n", weekly_means)
print("Trend slopes (steps, calories, mins, hr):", trend_slopes)
print("Month means (3 months):\n", month_means)
print("MoM growth rates between month1->2 and 2->3:\n", mom_growth)

print("\n=== CORRELATIONS & INSIGHTS ===")
print("Metric correlation matrix:\n", corr_matrix)
print(f"Age vs steps correlation: {age_steps_corr:.2f}")
print(f"Avg steps by gender → male: {avg_steps_male:.0f}, female: {avg_steps_female:.0f}")
print("Top 10 health-score users:", health_top10_users.tolist())

print("\n=== GOAL ACHIEVEMENT ===")
print("Users meeting all goals ≥80% of days:", consistent_achievers.size)
print("User IDs:", consistent_achievers.tolist())
