# src/feature_engineering.py
import pandas as pd
import logging

def add_features(df):
    """
    Adds technical indicators and target variable to the DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame with at least a 'Close' column.

    Returns:
    pd.DataFrame: DataFrame with added features or an empty DataFrame in case of an error.
    """
    try:
        df.drop(0, inplace = True)
        
        return df
    except Exception as e:
        # Log any errors that occur during feature engineering
        logging.error(f"Error in feature engineering: {e}")
        return pd.DataFrame()
