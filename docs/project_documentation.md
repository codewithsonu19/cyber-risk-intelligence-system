# CyRIQ Project Documentation

## 1. Project Introduction

CyRIQ is an AI-Powered Continuous Cyber Risk Quantification and Investment Optimization Platform.

It helps organizations identify cyber risks, calculate their financial impact, prioritize vulnerabilities, and select suitable security investments.

## 2. Problem Statement

Organizations face many cybersecurity risks, but it is difficult to understand which risks are most important and where security budget should be invested.

CyRIQ connects technical cybersecurity risk with financial impact to support better security investment decisions.

## 3. Main Objectives

- Identify and manage organizational assets.
- Analyze cybersecurity vulnerabilities.
- Quantify cyber risk.
- Estimate financial risk exposure.
- Prioritize high-risk vulnerabilities.
- Optimize cybersecurity investments.
- Provide data-driven security recommendations.

## 4. System Workflow

The main workflow of CyRIQ is:

Asset Inventory
↓
Vulnerability Analysis
↓
Risk Quantification
↓
Financial Exposure
↓
Investment Optimization
↓
Security Recommendation

## 5. Risk Quantification

CyRIQ calculates risk using:

Risk Exposure = Estimated Loss × Likelihood

Example:

Estimated Loss = ₹20 Lakh
Likelihood = 0.6

Risk Exposure = 20 × 0.6
Risk Exposure = ₹12 Lakh

## 6. Risk Scoring

CyRIQ considers:

- Asset Criticality
- CVSS Score
- Likelihood

These factors are combined to calculate an overall risk score.

## 7. Financial Analysis

CyRIQ calculates:

- Current Risk
- Expected Risk
- Risk Reduction
- Investment Cost
- ROI

ROI Formula:

ROI = ((Risk Reduction - Investment Cost) / Investment Cost) × 100

Example:

Risk Reduction = ₹9 Lakh
Investment Cost = ₹2 Lakh

ROI = ((9 - 2) / 2) × 100
ROI = 350%

## 8. Investment Optimization

CyRIQ compares different security investments based on:

- Cost
- Risk Reduction
- ROI
- Available Budget

The platform prioritizes affordable investments with better ROI.

## 9. Machine Learning

The ML module is used for risk prediction.

Main ML files:

- preprocessing.py
- feature_engineering.py
- train.py
- predict.py
- model.pkl

The trained model can predict a risk score using:

- Criticality
- CVSS Score
- Likelihood

## 10. Technology Stack

Backend:
- Python
- FastAPI

Frontend:
- Streamlit

Data Processing:
- Pandas

Machine Learning:
- Scikit-learn

Database:
- SQLite

## 11. API Modules

CyRIQ provides APIs for:

- Assets
- Vulnerabilities
- Risk Calculation
- Financial Analysis
- Investment Optimization

## 12. Frontend Modules

The frontend contains:

- Dashboard
- Asset Inventory
- Vulnerability Analysis
- Risk Quantification
- Financial Exposure
- Investment Optimization

## 13. Example Scenario

Customer Database:

- Criticality: 9/10
- CVSS: 9.8
- Likelihood: 0.6
- Estimated Loss: ₹20 Lakh
- Current Risk Exposure: ₹12 Lakh
- Expected Risk: ₹3 Lakh
- Risk Reduction: ₹9 Lakh

If MFA and patching cost ₹2 Lakh:

ROI = 350%

## 14. Conclusion

CyRIQ helps organizations understand cybersecurity risks in both technical and financial terms.

It supports continuous risk assessment and helps organizations make better cybersecurity investment decisions.