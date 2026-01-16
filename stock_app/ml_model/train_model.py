import yfinance as yf # type: ignore
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore

# Download stock data
data = yf.download("AAPL", start="2018-01-01")
close_prices = data[['Close']].values

scaler = MinMaxScaler()
scaled = scaler.fit_transform(close_prices)

X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i-60:i, 0])
    y.append(scaled[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape(X.shape[0], X.shape[1], 1)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(60, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, y, epochs=5, batch_size=32)

model.save("stock_app/ml_model/model.h5")
print("✅ Model trained and saved successfully")
