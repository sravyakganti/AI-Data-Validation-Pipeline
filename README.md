# AI-Data-Validation-Pipeline
Project Overview
This repository contains a **serverless-ready data quality pipeline** designed to validate large-scale workforce datasets. It combines traditional data engineering checks (Nulls/Duplicates) with **Unsupervised Machine Learning (Isolation Forest)** to detect complex anomalies that standard rule-based logic misses.

This logic is same as the solution I implemented to **reduce onboarding errors by 75%** and **improve data reliability scores**, as detailed in my professional experience.

## Business Value
*   **Risk Mitigation:** Automatically flags "impossible" values (e.g., negative salaries, excessive work hours) before they reach downstream payroll systems.
*   **Operational Efficiency:** Reduces manual data review time by auto-generating anomaly reports.
*   **Scalability:** Designed to handle high-volume datasets (simulated here with 1,000+ records).

## Tech Stack
*   **Language:** Python 3.9+
*   **Data Manipulation:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (Isolation Forest for Anomaly Detection)
*   **Data Generation:** Faker

## Project Structure
*   `main.py`: Orchestrates the ETL and Validation pipeline.
*   `ai_validator.py`: Contains the core `DataValidator` class and ML logic.
*   `data_generator.py`: Generates synthetic workforce data with intentional outliers to test the model.
*   `flagged_anomalies.csv`: The output file containing rows flagged by the AI as suspicious.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   Run the pipeline:
   python main.py
   ## The AI Approach
Unlike simple SQL constraints, this pipeline uses an Isolation Forest algorithm. It analyzes multi-dimensional features (Salary, WeeklyHours, RiskScore) to identify data points that deviate significantly from the statistical norm, effectively catching "unknown unknowns" in data quality.
