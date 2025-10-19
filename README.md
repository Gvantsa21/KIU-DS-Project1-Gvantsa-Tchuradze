# Project 1 — Python & NumPy Fundamentals

**Course:** Introduction to Data Science with Python
**Program:** Computer Science, Kutaisi International University

---

## Student

* **Name:** *Gvantsa Tchuradze*
* **Student ID:** not sure what student id is ... (Tchuradze.gvantsa@kiu.edu.ge?)
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


## Requirements

* Python 3.10+ recommended
* `numpy==1.24.3` (exact version required by course)

I
## How to run

**Python script:**

```bash
python Project1_GVantsa_Tchuradze.py
```
---

## Summary of findings (Task 3)

This project uses a simulated dataset of 100 users over 90 days with four daily metrics: steps, calories, active minutes, and average heart rate. I first added some problems to the data to make it realistic: about 5% missing values (NaNs) to imitate device failures and 2% extreme outliers. To clean the data I removed outliers using the IQR method for each metric, then filled missing values with the mean of that metric. Doing outlier removal first makes the mean used for imputation more reliable.

After cleaning, I looked for patterns:

Users naturally fall into three activity groups by average steps: low (≈25%), medium (≈50%), and high (≈25%).

The top 10 users (by a combined z-score across metrics) have higher steps, more active minutes, and burn more calories — so steps and calories are linked.

Some users are very consistent day-to-day (low variation), which is useful for making personalized suggestions.

Time patterns:

There is a weekly rhythm (day-of-week effect): activity usually dips slightly on weekends and is higher mid-week.

A 7-day rolling average smooths short-term noise and shows small trends over time.

I also compared three 30-day windows to check month-over-month changes.

Other findings:

Steps and calories are positively correlated. Active minutes also correlate with these. Heart rate has a weaker correlation with the others.

Age has a small negative link with steps (older users tend to have slightly fewer steps). Men and women show small differences in average steps.

I created a simple health score (weighted z-sum) that ranks users — weights put most emphasis on steps and active minutes.

Using goals (8000 steps, 2000 calories, 60 active minutes), a small group meets all three goals at least 80% of days.

Surprising note: Because steps were generated with a lognormal distribution and clipped to realistic values, the simulated data has more consistent achievers than purely random numbers would — so be careful: how you create synthetic data can change conclusions.


If you have questions about this repository, email: [Tchuradze.gvantsa@kiu.edu.ge](mailto:Tchuradze.gvantsa@kiu.edu.ge)

---

*Prepared for: Introduction to Data Science with Python — Project 1*
