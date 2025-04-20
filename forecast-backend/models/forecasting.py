import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from sklearn.impute import SimpleImputer
from statsmodels.tsa.api import VAR
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def run(data):
    print("validate required columns")
    # validate required columns
    required_columns = ['Date', 'Temp Max', 'Temp Min']

    missing_cols = [col for col in required_columns if col not in data.columns]
    if 0 < len(missing_cols):
        return pd.DataFrame([])
    print("select required columns")
    # select required columns
    df = data[required_columns]
    print("format date column to datetime")
    # format date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='raise')

    # clean data with ------
    df = df[~df.applymap(lambda x: x == '-----',).any(axis=1)]
    print("format all columns except date to float")
    # format all columns except date to float
    for col in df.columns:
        if col != "Date" and col in df.columns:
            df[col] = df[col].astype(float)
    print("fill empty values with mean strategy")
    df_wo_date = df[[col for col in required_columns if col != "Date"]]
    # fill empty values with mean strategy
    imputer = SimpleImputer(strategy='mean')

    # Fit and transform the dataframe
    df = pd.DataFrame(imputer.fit_transform(df_wo_date), columns=df_wo_date.columns)
    start_date = '1951-01-01'
    date_index = pd.date_range(start=start_date, periods=len(df), freq='D')
    df.index = date_index
    print("train LSTM model")
    # train LSTM model
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)

    def create_sequences(data, seq_length=30):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)

    sequence_length = 30
    X, y = create_sequences(scaled_data, sequence_length)
    train_size = int(0.9 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]


    model = Sequential()
    model.add(LSTM(64, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=False))
    model.add(Dense(2))  # 4 outputs for 4 temperature features
    model.compile(optimizer='adam', loss='mse')
    model.summary()

    model.fit(X_train, y_train, epochs=30, batch_size=32, validation_split=0.1, verbose=1)

    y_pred = model.predict(X_test)
    y_pred_inv = scaler.inverse_transform(y_pred)
    y_test_inv = scaler.inverse_transform(y_test)
    print("Forecast data")
    forecast_input = scaled_data[-sequence_length:].copy()  # shape (30, 4)
    forecast = []

    for _ in range(365):
        input_seq = np.expand_dims(forecast_input[-sequence_length:], axis=0)  # (1, 30, 4)
        next_day = model.predict(input_seq, verbose=0)[0]  # (4,)
        forecast.append(next_day)
        forecast_input = np.vstack([forecast_input, next_day])

    forecast = np.array(forecast)  # shape (365, 4)
    forecast_rescaled = scaler.inverse_transform(forecast)
    last_date = df.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=365, freq='D')

    forecast_df = pd.DataFrame(forecast_rescaled, columns=df.columns, index=future_dates)

    return forecast_df
       

