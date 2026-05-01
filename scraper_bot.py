import os
import json
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ADMIN_CHAT_ID")

PRICES_FILE = "tg/saved_prices.json"

PRODUCTS = [
    {
        "name": "A Light in the Attic",
        "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    },
    {
        "name": "Tipping the Velvet",
        "url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    },
    {
        "name": "Soumission",
        "url": "https://books.toscrape.com/catalogue/soumission_998/index.html"
    },
]

CHECK_INTERVAL = 60


def get_price(url: str) -> float | None:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, "html.parser")

        price_tag = soup.select_one("p.price_color")

        if not price_tag:
            print(f"Price not found at {url}")
            return None

        price_text = price_tag.text.strip().replace("£", "").replace("Â", "")
        return float(price_text)

    except Exception as e:
        print(f"Error parsing at {url}: {e}")
        return None


def send_telegram(message: str) -> None:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}

    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram send error: {e}")


def load_saved_prices() -> dict:
    if os.path.exists(PRICES_FILE):
        with open(PRICES_FILE, "r") as f:
            return json.load(f)
    return {}  


def save_prices(prices: dict) -> None:
    with open(PRICES_FILE, "w") as f:
        json.dump(prices, f, indent=2)


def check_prices() -> None:
    saved = load_saved_prices()
    updated = {}

    for product in PRODUCTS:
        name = product["name"]
        url = product["url"]

        current_price = get_price(url)

        if current_price is None:
            continue

        updated[name] = current_price

        if name not in saved:
            print(f"[First run] {name}: £{current_price}")
            continue

        old_price = saved[name]

        if current_price != old_price:
            direction = "📈 Зросла" if current_price > old_price else "📉 Впала"
            diff = abs(current_price - old_price)

            message = (
                f"🔔 <b>Price change!</b>\n\n"
                f"📦 Product: {name}\n"
                f"{direction}: £{old_price} → £{current_price}\n"
                f"Difference: £{diff:.2f}\n\n"
                f"🔗 {url}"
            )

            send_telegram(message)
            print(f"Alert sent: {name} {old_price} → {current_price}")
        else:
            print(f"No change: {name} — £{current_price}")

    save_prices(updated)


def main():
    print(f"Price monitoring started. Checking every {CHECK_INTERVAL} sec.\n")
    send_telegram("✅ Price monitoring started!")

    while True:
        print(f"\n--- Checking prices ---")
        check_prices()
        print(f"Next check in {CHECK_INTERVAL} sec...")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()