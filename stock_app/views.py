from django.shortcuts import render # type: ignore
import yfinance as yf # type: ignore
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model # type: ignore
from django.conf import settings # type: ignore
import os

# ---------------- MODEL LOAD ----------------
MODEL_PATH = os.path.join(
    settings.BASE_DIR, "stock_app", "ml_model", "model.h5"
)

model = load_model(MODEL_PATH) if os.path.exists(MODEL_PATH) else None


# ---------------- RSI FUNCTION ----------------
def compute_rsi(series, period=14):
    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # 🔥 FORCE SINGLE FLOAT
    return float(rsi.iloc[-1])


# ---------------- DASHBOARD VIEW ----------------
def dashboard(request):
    stock = request.GET.get("symbol", "AAPL")

    data = yf.download(stock, start="2020-01-01", progress=False)
    close = data[["Close"]]

    if len(close) < 60:
        return render(request, "dashboard.html", {
            "error": "Not enough data"
        })

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(close)

    last_60 = scaled[-60:]
    X_test = last_60.reshape(1, 60, 1)

    prediction = model.predict(X_test, verbose=0)
    prediction = scaler.inverse_transform(prediction)[0][0]

    # ✅ FIXED RSI
    rsi = compute_rsi(close["Close"])

    # ✅ SAFE SIGNAL LOGIC
    if rsi < 30:
        signal = "BUY"
    elif rsi > 70:
        signal = "SELL"
    else:
        signal = "HOLD"

    context = {
        "stock": stock,
        "price": round(float(close.iloc[-1, 0]), 2),
        "prediction": round(float(prediction), 2),
        "rsi": round(float(rsi), 2),
        "signal": signal,
    }

    return render(request, "dashboard.html", context)
