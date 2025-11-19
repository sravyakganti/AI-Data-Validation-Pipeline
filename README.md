AI & GenAI Workforce Data Pipeline

## Project Overview
This repository contains a dual-layer analytics pipeline designed for financial and workforce data.
1.  **Anomaly Detection:** Uses **Isolation Forest (ML)** to mathematically detect payroll outliers.
2.  **GenAI Reporting:** Uses a **Large Language Model (LLM)** (DistilGPT-2 via Transformers) to automatically generate natural language risk summaries for non-technical stakeholders.

## Business Value
*   **Automated Insights:** Replaces manual report writing with AI-generated executive summaries.
*   **Risk Mitigation:** Detects payroll errors (e.g., negative salaries) before processing.

## Tech Stack
*   **GenAI / LLM:** Hugging Face Transformers (DistilGPT-2)
*   **Machine Learning:** Scikit-Learn (Isolation Forest)
*   **Language:** Python 3.9+
