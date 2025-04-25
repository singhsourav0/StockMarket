# 📈 Stock Data Analysis using Nifty & Sensex

A streamlined process to fetch historical stock prices (Nifty & Sensex) from Yahoo Finance, store them in a MySQL local server, clean the data using SQL and Python commands, reload the cleaned data, and visualize insights using Streamlit.

---

## 🚀 Tech Stack

- Python (Pandas, yFinance, Streamlit)
- MySQL (via MySQL Connector/Python)
- Data Visualization: Streamlit

---

## 🔁 Workflow

1. **Fetch Data**: Nifty & Sensex from Yahoo Finance
2. **Store in MySQL**: Table `stock_prices`
3. **Clean Data**: Use SQL and Python commands to handle nulls, fix dates, and remove anomalies
4. **Reload Cleaned Data**: Store cleaned data back into MySQL
5. **Visualize**: Generate plots and insights using Streamlit

---

## 📂 Folder Breakdown

| Folder | Description |
|--------|-------------|
| `src/` | Python scripts for data fetching, cleaning, and visualization |
| `sql/` | SQL scripts for schema and data cleaning |
| `data/` | Local CSV backup (optional) |

---

## 🛠️ Run Instructions

1. Clone the repo  
2. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:  
    ```bash
    streamlit run src/app.py
    ```
