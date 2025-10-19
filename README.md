🧮 Project 1 

Course: Introduction to Data Science with Python
Student: Gvantsa Tchuradze
Date: October 19, 2025
Honor Code: I confirm that this submission is entirely my own work and that no part has been plagiarized.

🌐 Project Description

This project showcases essential programming and data analysis skills using Python and NumPy.
It includes three interconnected tasks that gradually move from basic Python logic to applied numerical data exploration.

No.	Task Title	Core Topic	Grade Weight
1	Working with Python Data Structures	Dictionaries, control flow, and functions	2%
2	Exploring NumPy Arrays	Array generation, slicing, aggregation	2%
3	Simulated Data Analysis	Practical fitness dataset simulation and analytics	2%

Total Contribution: 6% of course grade
Submission Deadline: Week 4, Sunday at 23:59 (GT)

🔹 Task 1 — Python Data Structures and Logic

A small-scale system to evaluate and summarize student performance using core Python features.

Core Components

A dictionary named students storing:

student name

test scores

attendance records

Functions to:

compute averages and letter grades

determine pass/fail based on attendance and grades

list top-performing students

summarize grade distribution

Expected Output

Overall class performance report

Top 5 students with grades

List of failed students and reasons

Grade distribution summary table

🔹 Task 2 — NumPy Arrays and Analytical Operations

This section demonstrates efficient numerical manipulation using NumPy arrays.

Main Goals

Array Initialization:

Daily temperatures dataset (365×5)

Yearly sales data (12×4)

Identity, evenly spaced, and reshaped arrays

Indexing & Selection:

Extract data by time periods or conditions (months, weekends, etc.)

Boolean & Fancy Indexing:

Identify extreme values (hot/cold days)

Apply masks and data replacements

Statistical Computations:

Mean, median, variance, correlations, and moving averages

Sales Analytics:

Total sales per category, best month detection, and category comparison

🔹 Task 3 — Fitness Data Simulation and Analysis

A complete analytical workflow built exclusively with NumPy, simulating daily fitness activity for 100 users over 90 days.

Dataset Details

Shape: (100, 90, 4) → users × days × [steps, calories, active minutes, heart rate]

Value ranges:

Steps: 2000–15000

Calories: 1500–3500

Active minutes: 20–180

Heart rate: 60–120 bpm

Data Enrichment

5% missing values (sensor malfunction simulation)

2% outliers (unrealistic activity spikes)

Metadata array: [user_id, age (18–70), gender (0 = female, 1 = male)]

Data Cleaning Functions

handle_missing(data) — replaces NaN values with column means

remove_outliers(data, metric_index) — detects outliers via IQR and replaces them with median values

The pipeline ensures the dataset remains complete and realistic after cleaning.

Analytical Components

User-Level Insights:

Mean performance, top 10 active users, consistency evaluation

Activity classification by overall engagement level

Time-Based Analysis:

Weekly averages, rolling 7-day trends, and linear change estimation

Correlations & Demographics:

4×4 metric correlation matrix

Relationship between age, gender, and activity

Computation of a composite Health Index

Goal Achievement Tracking:

Success if: steps ≥ 8000, calories ≥ 2000, minutes ≥ 60

Users achieving all goals ≥80% of the time identified

📈 Findings Overview
Aspect	Main Observation
Avg. daily steps	Around 8,000–9,000
Steps ↔ Active minutes	Strong positive correlation
Age vs activity	Slight negative trend
Gender comparison	Males slightly more active overall
Highly consistent users	15–20 participants met goals 80%+
General trend	Gradual improvement over 3 months
🧩 Interpretations

7-day moving averages revealed weekly cycles, with weekends showing reduced activity.

Daily steps, calories, and active minutes are closely interrelated.

Heart rate patterns show weaker links, likely due to personal physiological differences.

Activity declines slightly with increasing age.

A standardized “health score” derived from z-scores provides a balanced user comparison metric.

💬 Suggestions
For Individuals

Aim for consistent daily effort rather than short bursts.

Focus on achieving at least two goals per day (steps, calories, minutes).

For App Developers

Add weekly trend summaries and visual dashboards.

Implement streak badges and adaptive daily targets for better user motivation.

For Marketing Teams

Engage moderately active users (middle 50%) through group challenges.

Support less active users via tailored goal reminders and milestone rewards.

⚙️ How to Execute the Project

Download or clone the project folder.

Ensure the environment meets requirements:

Python >= 3.9  
NumPy >= 1.24.3


Run the following scripts sequentially:

python task1.py
python task2.py
python task3.py
