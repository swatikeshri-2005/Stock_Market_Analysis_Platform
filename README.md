# 📈 AI-Powered Stock Market Analysis Platform (Django + ML)

An end-to-end **AI-based Stock Market Analysis Web Application** built using **Django**, **Machine Learning (LSTM)**, and **yFinance**. The platform fetches real-time stock data, predicts next-day prices, calculates technical indicators (RSI), and generates **BUY / SELL / HOLD** signals.

This project is suitable for:

* 🎓 Final Year / Major Project
* 💼 Resume & Portfolio
* 📊 Learning Django + ML integration

---

## 🚀 Features

* 📡 Real-time stock data using **yFinance**
* 🧠 LSTM-based **Next-Day Stock Price Prediction**
* 📉 Technical Indicator: **RSI (Relative Strength Index)**
* 📌 Automated **BUY / SELL / HOLD** signals
* 🌐 Web dashboard built with **Django**
* 🔄 Dynamic stock symbol search

---

## 🛠️ Tech Stack

| Layer           | Technology                |
| --------------- | ------------------------- |
| Backend         | Django 5.x                |
| ML Model        | TensorFlow / Keras (LSTM) |
| Data Source     | yFinance                  |
| Data Processing | Pandas, NumPy             |
| ML Utilities    | Scikit-learn              |
| Frontend        | HTML (Django Templates)   |
| Language        | Python 3.10               |

---

## 📂 Project Structure

```
Stock Market Analysis Platform/
│
├── manage.py
├── stock_market_ai/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── stock_app/
│   ├── views.py
│   ├── urls.py
│   ├── ml_model/
│   │   └── model.h5
│   └── templates/
│       └── dashboard.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/stock-market-analysis-platform.git
cd stock-market-analysis-platform
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django tensorflow yfinance pandas numpy scikit-learn
```

---

## ▶️ Run the Project

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

Try different stocks:

```
http://127.0.0.1:8000/?symbol=AAPL
http://127.0.0.1:8000/?symbol=TSLA
```

---

## 📊 Output Example

* **Current Stock Price**
* **Predicted Next-Day Price**
* **RSI Value**
* **Trading Signal (BUY / SELL / HOLD)**

---

## 🧠 Machine Learning Model

* Model Type: **LSTM (Long Short-Term Memory)**
* Input: Last 60 days closing prices
* Scaling: MinMaxScaler
* Output: Next-day predicted price

---

## ⚠️ Notes

* Stock prices are fetched in **USD** (via yFinance)
* Ensure `model.h5` exists in `stock_app/ml_model/`
* This project is for **educational purposes only**, not financial advice

---

## 🔮 Future Enhancements

* 📊 Interactive charts (Plotly)
* 📰 News sentiment analysis
* 🔐 User authentication & watchlist
* 📈 Advanced indicators (MACD, EMA)
* ☁ Cloud deployment

---

## 👩‍💻 Author

**Swati Keshri**
AI & ML Enthusiast | Django Developer

---

## ⭐ Support

If you like this project, please ⭐ star the repository on GitHub!
