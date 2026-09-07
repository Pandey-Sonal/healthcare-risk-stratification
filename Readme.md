# Healthcare Patient Risk Stratification & Predictive Analytics

## 📌 Project Overview

An end-to-end healthcare analytics project designed to analyze patient data, identify risk patterns, and predict patient risk using machine learning.

The project combines SQL, Excel, Python, machine learning, and Streamlit to demonstrate a complete healthcare analytics workflow from raw data analysis to interactive risk prediction.

---

## 🎯 Project Objectives

- Analyze patient demographics, diagnoses, laboratory results, and outcomes.
- Identify abnormal laboratory patterns.
- Analyze treatment costs and patient outcomes.
- Engineer meaningful features from patient data.
- Build a machine learning classification model for patient risk prediction.
- Develop an interactive Streamlit application for risk assessment.

---

## 🔄 Project Workflow

```text
Patient Data
     ↓
PostgreSQL / SQL Analysis
     ↓
Excel Analysis & KPIs
     ↓
Python Data Cleaning
     ↓
Feature Engineering
     ↓
Machine Learning
     ↓
Risk_model1.pkl
     ↓
Streamlit Application
     ↓
Patient Risk Prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- PostgreSQL
- SQL
- Excel
- Streamlit
- Joblib
- Jupyter Notebook

---

## 📊 Data Analysis

SQL was used to perform:

- Patient and laboratory data joins
- Average laboratory result analysis
- Abnormal laboratory result identification
- Treatment cost analysis by diagnosis
- Patient outcome analysis
- Laboratory trend analysis
- Outcome distribution by diagnosis

Excel was used for:

- VLOOKUP-based data preparation
- Patient data enrichment
- Risk classification
- KPI and trend analysis

---

## 🤖 Machine Learning

Python and Pandas were used for:

- Data cleaning
- Dataset merging
- Date conversion
- Length of Stay calculation
- Outcome encoding
- Feature preparation
- Train/test splitting

A machine learning classification model was trained and saved using Joblib:

```text
Risk_model1.pkl
