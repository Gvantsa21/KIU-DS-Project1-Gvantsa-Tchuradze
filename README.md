# Project 1 — Python & NumPy Fundamentals

**Course:** Introduction to Data Science with Python
**Program:** Computer Science, Kutaisi International University

---

## Student

* **Name:** *Gvantsa Tchuradze*
* **Student ID:** *SXXXX*
* **Submission Date:** *2025-10-19*

**Honor Code:** I certify that this work is my own and I have not plagiarized.

---

## Project Overview

This repository contains the solution for **Project 1: Python & NumPy Fundamentals** (October 2025). The project implements three tasks:

* **Task 1 — Python Data Structures & Control Flow**: processing student exam scores and attendance using pure Python.
* **Task 2 — NumPy Arrays & Operations**: creating, exploring, and analyzing temperature and sales arrays.
* **Task 3 — Applied Data Analysis**: simulated fitness-tracking dataset (100 users × 90 days × 4 metrics), cleaning pipeline and analysis using NumPy.

This repository is prepared according to the course submission guidelines and verified to run without errors (restart kernel & run all).

---

## Repository structure

```
KIU-DS-Project1-FirstName-LastName/
├─ Project1_FirstName_LastName.ipynb   # Preferred submission (Jupyter Notebook)
├─ Project1_FirstName_LastName.py      # Or Python script version
├─ README.md                           # This file
├─ requirements.txt                     # numpy==1.24.3
├─ .gitignore                           # recommended (pycache, .ipynb_checkpoints)
└─ data/                                # (optional) sample outputs or saved CSVs
```

---

## Requirements

* Python 3.10+ recommended
* `numpy==1.24.3` (exact version required by course)

Install dependencies with:

```bash
pip install -r requirements.txt
```

`requirements.txt` content (required by course):

```
numpy==1.24.3
```

---

## How to run

**Python script:**

```bash
python Project1_FirstName_LastName.py
```

Make sure the script prints the requested outputs for each task (Course statistics, top performers, temperature and sales analyses, Task 3 console summary, etc.).

---

## Summary of findings (Task 3)

*This section provides the required analysis summary of the simulated fitness dataset (≥300 words).*

The simulated dataset models 100 users across 90 days with 4 metrics: daily steps, calories, active minutes, and average heart rate. After introducing realistic data issues (5% random NaNs to mimic device failures and 2% extreme outliers) the data cleaning pipeline removed outliers using the IQR method per metric and then replaced missing values with per-metric means. This two-step approach reduces bias from extreme values when computing imputation values. The cleaned dataset enables reliable per-user aggregation and population-level temporal analysis.

Key user behavior patterns show a diversified activity distribution. Users cluster into three activity bands (Low/Medium/High) based on step percentiles: roughly 25% low, 50% medium, 25% high. The top 10 active users (by combined z-score across metrics) show consistent high daily step counts, elevated active minutes, and slightly higher-than-average calorie burn, suggesting a correlation between steps and calories. Consistency analysis (lowest mean std deviation across metrics) highlights a subset of users with predictable daily routines — useful for personalized recommendations.

Temporal trends reveal weekly periodicity with day-of-week effects: higher activity on mid-week days and small dips on weekends for the aggregate population, though subgroups behave differently. A 7-day rolling mean smooths daily volatility and uncovers subtle increasing/decreasing trends; linear slope estimation per metric is used to quantify trend directions. Month-over-month growth (three 30-day windows) provides coarse-grained seasonality — useful for marketing campaigns or feature-testing windows.

Correlation analysis indicates expected relationships: steps and calories are positively correlated; active minutes correlate with steps and calories; average heart rate correlates weakly with other metrics. Age shows a modest negative correlation with average steps, while gender-based averages differ slightly — insights that can inform targeted interventions.

Health score (a weighted z‑sum) ranks users by a composite measure; selecting weights (0.4 steps, 0.2 calories, 0.35 active_minutes, 0.05 heart rate) emphasizes physical activity. Goal achievement analysis (8000 steps, 2000 calories, 60 active minutes) reports the fraction of days each user meets all goals; a small subset meets goals ≥80% of days and can be considered consistent achievers for rewards or beta features.

**Most surprising finding:** The dataset often shows more consistent achievers than purely random data would suggest because of the lognormal steps generation and clipping that concentrates values around realistic daily step medians — a reminder that synthetic data choices strongly shape downstream conclusions.

**Recommendations:** (1) Use targeted nudges for medium-activity users to convert them to higher engagement; (2) Investigate device reliability and missingness patterns before production deployment; (3) Consider per-user baselines when defining goals to avoid penalizing older or less active users unjustly. Further improvements include richer metadata (occupation, device type) and longer time windows to assess retention effects.


If you have questions about this repository, email: [your.email@example.com](mailto:your.email@example.com)

---

*Prepared for: Introduction to Data Science with Python — Project 1*
