import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.load_data import load_from_sql
from src.feature_engineering import add_features

st.set_page_config(page_title="📊 Stock Market Analysis", layout="wide")

# --- MySQL credentials ---
host = "127.0.0.1"
user = "root"
password = "**********"
database = "stocksql"

# --- Load cleaned data from SQL ---
@st.cache_data
def load_and_process_data(raw_table):
    df_cleaned = load_from_sql(host, user, password, database, raw_table)
    if not df_cleaned.empty:
        df_final = add_features(df_cleaned)
        df_final['Date'] = pd.to_datetime(df_final['Date'])
        df_final['Year'] = df_final['Date'].dt.year
        df_final['Close'] = pd.to_numeric(df_final['Close'], errors='coerce')
        return df_final
    return pd.DataFrame()

# --- Streamlit UI ---
st.title("📈 Stock Market Analysis Dashboard")

# Dropdown for selecting dataset
dataset_options = {"NIFTY": "stock_nifty", "SENSEX": "stock_sensex"}
selected_dataset = st.sidebar.selectbox("Select Dataset", options=list(dataset_options.keys()), index=0)
raw_table = dataset_options[selected_dataset]

df = load_and_process_data(raw_table)

if df.empty:
    st.warning(f"No data available for {selected_dataset}. Please run main pipeline to generate data.")
else:
    st.subheader(f"📅 Time Series - Closing Price (Yearly Mean) ({selected_dataset})")
    yearly_mean = df.groupby('Year')['Close'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=yearly_mean, x='Year', y='Close', ax=ax, color='blue')
    ax.set_title(f"Yearly Mean Closing Price ({selected_dataset})")
    st.pyplot(fig)

    st.subheader(f"📈 Year-wise Closing Price Stats ({selected_dataset})")
    summary = df.groupby('Year')['Close'].agg(['first', 'last'])
    summary['Growth (%)'] = ((summary['last'] - summary['first']) / summary['first']) * 100
    st.dataframe(summary.style.format({"Growth (%)": "{:.2f}"}), use_container_width=True)

    st.subheader(f"📊 Volume Traded Over Time ({selected_dataset})")
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')  # Ensure 'Volume' is numeric
    yearly_mean = df.groupby('Year')['Volume'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=yearly_mean, x='Year', y='Volume', ax=ax2, color='orange')  # Use seaborn for consistency
    ax2.set_title(f"Volume Over Time ({selected_dataset})")
    st.pyplot(fig2)
