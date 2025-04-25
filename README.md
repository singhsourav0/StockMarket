# 📈 Stock Trend Predictor using Nifty & Sensex

A full pipeline to fetch historical stock prices (Nifty & Sensex) from Yahoo Finance, store and clean them in SQL Server, perform feature engineering, train machine learning models (Random Forest & XGBoost), and log predictions back into SQL for analytics and dashboards.

---

## 🚀 Tech Stack

- Python (Pandas, yFinance, Scikit-learn, XGBoost)
- SQL Server (via pyodbc + SQLAlchemy)
- Machine Learning: Random Forest, XGBoost

---

## 🔁 Pipeline Workflow

1. **Fetch Data**: Nifty & Sensex from Yahoo Finance
2. **Store in SQL Server**: Table `stock_prices`
3. **Clean using SQL**: Remove nulls, low volume, fix date
4. **Feature Engineering**: MA, RSI, Returns
5. **Train ML Models**: Predict Up/Down Trend
6. **Store Predictions**: Log into `stock_predictions` table

---

## 📂 Folder Breakdown

| Folder | Description |
|--------|-------------|
| `src/` | Core Python scripts for each stage of the pipeline |
| `sql/` | (Optional) SQL scripts for schema management |
| `data/` | Local CSV backup (optional) |

---

## 🛠️ Run Instructions

1. Clone the repo  
2. Install dependencies:
