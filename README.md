# 📊 Price Monitor Bot

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Notifications-26A5E4?style=flat-square&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Automated price monitoring tool that scrapes product pages and sends Telegram alerts when prices change. Set it up once — get notified instantly whenever a price drops or rises.

---

## ✨ Features

- 🔍 Scrapes any product page on a schedule
- 📉 Detects price drops and increases
- 🔔 Instant Telegram notification with price diff
- 💾 Saves price history between runs (JSON storage)
- ⚙️ Easy to add new products — just add URL to the list
- 🔗 Direct product link included in every notification

---

## 📱 Notification Example

```
🔔 Price Change Detected!

📦 Product: A Light in the Attic
📉 Dropped: £51.77 → £40.00
Difference: £11.77

🔗 https://books.toscrape.com/...
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/price-monitor.git
cd price-monitor
```

### 2. Install dependencies
```bash
pip install requests beautifulsoup4 python-dotenv
```

### 3. Set up environment variables
Create a `.env` file:
```
BOT_TOKEN=your_telegram_bot_token
ADMIN_CHAT_ID=your_chat_id
```

### 4. Add products to monitor
Edit `scraper_bot.py`:
```python
PRODUCTS = [
    {
        "name": "Product Name",
        "url": "https://example.com/product-page"
    },
]
```

### 5. Set the CSS selector for price
Find the price element on your target website using browser DevTools (F12):
```python
price_tag = soup.select_one("p.price_color")  # update this for your site
```

### 6. Set check interval
```python
CHECK_INTERVAL = 3600  # check every hour (in seconds)
```

### 7. Run
```bash
python scraper_bot.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| requests | HTTP requests |
| BeautifulSoup4 | HTML parsing |
| Telegram Bot API | Notifications (no extra library needed) |
| JSON | Price history storage |

---

## 📁 Project Structure

```
price-monitor/
├── scraper_bot.py      # Main monitoring script
├── saved_prices.json   # Auto-generated price history
├── .env.example        # Environment variables template
├── requirements.txt    # Dependencies
└── README.md
```

---

## 💡 Use Cases

- Monitor competitor prices
- Track deals on e-commerce sites
- Alert when flight or hotel prices drop
- Watch crypto or stock prices (via API)

---

## ⚠️ Note

Always check a website's Terms of Service before scraping. This tool is intended for personal use and legitimate business monitoring.

---

## 📄 License

MIT — feel free to use for commercial projects.
