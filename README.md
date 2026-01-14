# Real-Time Stock Market Analysis & Prediction System

## 📌 Project Overview
This project is a **generic, reusable stock market analysis and prediction system** built using Python and machine learning techniques.  
Instead of being limited to a specific company, the system allows users to **input any stock ticker** and automatically:

- Fetch historical stock price data
- Incorporate external market factors
- Perform exploratory data analysis (EDA)
- Prepare data for machine learning models
- Evaluate prediction performance

The goal is to move beyond simple historical price modeling and build a **market-aware prediction pipeline**.

---

## 🎯 Key Objectives
- Build a reusable pipeline for **any stock ticker**
- Fetch real-time and historical stock market data
- Include **macro and market-wide factors** that influence stock movement
- Perform clear, explainable exploratory data analysis
- Prepare data for machine learning and deep learning models
- Evaluate model accuracy honestly and transparently

---

## 🔤 User-Driven Design
This project is designed so that **no code changes are required** to analyse a new stock.

Users simply provide a stock ticker (e.g. `AAPL`, `TSLA`, `NVDA`) as input, and the same pipeline runs end-to-end.

---

## 📊 Data Sources

### Stock-Specific Data
- Open, High, Low, Close prices
- Volume
- Daily returns  
(Source: Yahoo Finance via `yfinance`)

### External Market Factors
To avoid relying only on historical prices, the project also includes:

- **S&P 500 Index (`^GSPC`)** – overall market movement
- **NASDAQ Index (`^IXIC`)** – tech-heavy market trend
- **VIX (`^VIX`)** – market volatility / fear index
- **US 10-Year Treasury Yield (`^TNX`)** – interest rate proxy

These features help capture **broader market conditions** that affect stock prices.

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- yFinance
- TensorFlow / Keras (planned)
- Google Colab (execution environment)
- GitHub (version control)

---



