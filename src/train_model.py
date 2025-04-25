import pandas as pd
# src/train_model.py
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import logging

def train_models(df):
    try:
        features = ['MA_5', 'MA_20', 'Return']
        X = df[features]
        y = df['Target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
        logging.info("Random Forest Report:\n" + classification_report(y_test, rf.predict(X_test)))

        xgb = XGBClassifier()
        xgb.fit(X_train, y_train)
        logging.info("XGBoost Report:\n" + classification_report(y_test, xgb.predict(X_test)))

        df['Prediction_RF'] = rf.predict(X)
        df['Prediction_XGB'] = xgb.predict(X)

        return df
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        return pd.DataFrame()

