# 📈 Trading Bot (Binance Futures Testnet)

## 🚀 Overview

This project is a Python-based trading bot that interacts with Binance Futures Testnet (USDT-M).
It allows users to place MARKET and LIMIT orders via CLI with proper validation, logging, and error handling.

---

## 🛠️ Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input
* Input validation
* Error handling
* Logging to file (`bot.log`)
* Clean modular structure

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
├── bot.log
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env` file

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

---

## ▶️ Usage

### ✅ MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### ✅ LIMIT Order (SELL)

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000
```

### ✅ LIMIT Order (BUY)

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 65000
```

---

## 📊 Sample Output

```
✅ Order Placed Successfully
Order ID      : 123456789
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00
```

---

## 📝 Logging

* Logs are stored in `bot.log`
* Includes:

  * API requests
  * Responses
  * Errors

---

## ⚠️ Notes / Assumptions

* Uses Binance Futures Testnet (not real trading)
* Orders may remain in `NEW` state due to low testnet liquidity
* LIMIT orders must follow:

  * BUY → price below market
  * SELL → price above market

---

## 🧠 Tech Stack

* Python 3
* python-binance
* argparse
* logging

---

## 👤 Author

Patneedi Naga Venkata Sri Sailaja
