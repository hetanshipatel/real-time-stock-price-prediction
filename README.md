# 📈 Stock Market Real-Time Prediction (User-Selectable Stocks)

This repository contains an **end-to-end, user-driven data science project** for stock market analysis and prediction.
The project is designed so **any user can input a stock ticker of their choice** (e.g., NVDA, NFLX, AAPL, TSLA) and:

* Fetch real-time & historical data
* Perform EDA & feature engineering
* Train and evaluate prediction models
* Check model accuracy before trusting predictions

The model **does not rely only on historical prices** — it also incorporates **external features** that influence stock movement.

---

## 🎯 Project Goals

* Build a **reusable & scalable stock prediction pipeline**
* Allow **dynamic stock input** instead of hardcoded companies
* Combine:

  * Historical price data
  * Technical indicators
  * Market & macro signals
* Keep everything **GitHub + Google Colab friendly**

---

## 🧠 Key Features

✔ User inputs stock ticker (no fixed company)
✔ Automatic data fetching
✔ One notebook for:

* EDA
* Feature engineering
* Model training
* Model evaluation

✔ Accuracy metrics clearly shown
✔ Extendable to real-time prediction later

---

## 📁 Repository Structure

```
stock-market-prediction/
│
├── data/
│   ├── raw/                # Raw fetched data (auto-generated)
│   └── processed/          # Cleaned & feature-engineered data
│
├── notebooks/
│   └── 01_stock_price_prediction_pipeline.ipynb
│
├── src/
│   ├── data_fetcher.py     # Fetch stock & external data
│   ├── feature_engineering.py
│   ├── model.py            # ML models
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Data Sources

### 1️⃣ Stock Price Data

Fetched dynamically using **user-input ticker**:

* Open
* High
* Low
* Close
* Volume

(Source: Yahoo Finance via `yfinance`)

### 2️⃣ External Factors (Not Just History!)

We include features that affect stock movement:

* 📉 Market index (S&P 500 / NASDAQ)
* 📊 Technical indicators:

  * Moving Averages (MA, EMA)
  * RSI
  * MACD
  * Volatility
* 🌍 Macro signals (optional later):

  * Interest rates
  * VIX (fear index)
* 🗞 Sentiment-ready structure (future extension)

---

## 📓 Notebook Explanation

### `01_data_collection_eda_feature_model.ipynb`

This **single notebook** performs:

1️⃣ User Input

```python
stock_ticker = input("Enter stock ticker (e.g., AAPL, NVDA): ")
```

2️⃣ Data Fetching
3️⃣ Exploratory Data Analysis (EDA)
4️⃣ Feature Engineering
5️⃣ Train/Test Split
6️⃣ Model Training
7️⃣ Model Evaluation (RMSE, MAE, R²)

✔ Clear outputs at every step

---

## 🤖 Models Used

* Linear Regression (baseline)
* Random Forest Regressor
* XGBoost (optional)
* LSTM (future extension)

We **evaluate accuracy first** before using predictions.

---

## 🚀 How to Run (GitHub Website Only)

1. Open the repository
2. Go to `notebooks/`
3. Open the notebook
4. Click **"Open in Colab"**

*No local setup required.*

---

## ☁️ Run on Google Colab (Recommended)

1. Open Google Colab
2. Click **File → Open notebook → GitHub**
3. Paste repo URL
4. Select the notebook
5. Run cells top to bottom

📌 Colab automatically installs dependencies

---

## 🧪 Accuracy & Validation

* Predictions are **not blindly trusted**
* Metrics shown clearly
* Comparison plots included

If accuracy is poor → model tuning required ❌
If accuracy is acceptable → predictions can be explored ✅

---

## 🔮 Future Enhancements

* Real-time prediction pipeline
* News & Twitter sentiment analysis
* Multiple-stock portfolio analysis
* Streamlit dashboard
* Auto model selection

---

## 🧑‍💻 Author

**Hetanshi Kachhiya Patel**
Data Scientist | ML | Analytics

---

⭐ If you like this project, star the repo and fork it!
