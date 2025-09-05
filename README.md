# Crypto Telegram Bot

> A simple Python Telegram bot that fetches real‑time cryptocurrency prices (via CoinGecko) and replies to user commands.

---

## Table of contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Project structure](#project-structure)
5. [Usage](#usage)
6. [Push to GitHub](#push-to-github)
7. [Extending the bot (ideas)](#extending-the-bot-ideas)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features

* Fetches real-time price for a given coin from CoinGecko.
* Simple command interface via Telegram (`/start`, `/price <coin>`).
* Easy to extend (alerts, top coins, multi-currency support).

---

## Prerequisites

* Python 3.9+
* `pip`
* A Telegram bot token (get one from \[@BotFather] on Telegram)
* (Optional) Git & GitHub account if you want to push the project

---

## Installation

1. Clone or create your project folder and place `crypto_bot.py` inside it.

2. Create a Python virtual environment and activate it (recommended):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install python-telegram-bot requests python-dotenv
```

> Optionally create a `requirements.txt` to pin dependencies:

```text
python-telegram-bot
requests
python-dotenv
```

---

## Project structure (example)

```
crypto-telegram-bot/
├─ crypto_bot.py
├─ requirements.txt
└─ README.md
```

---

## Usage

The example bot included in this project has the following minimal commands:

* `/start` — prints a short welcome message
* `/price <coin>` — returns the USD price for the specified coin (use CoinGecko `id`s such as `bitcoin`, `ethereum`, `dogecoin`)

### Running the bot

1. Make sure your bot token is set inside the code (`BOT_TOKEN = "your-token-here"`).

2. Run the script:

```bash
python crypto_bot.py
```

3. Open Telegram, start your bot and try:

```
/price bitcoin
/price ethereum
```

---

## Push to GitHub (quick steps)

1. Initialize git (if not already):

```bash
git init
git add .
git commit -m "Initial commit - Crypto Telegram Bot"
```

2. Create a new repo on GitHub, then push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

## Extending the bot (ideas)

* Add `/top` to return top N coins by market cap.
* Add alerting: `!alert btc > 60000` that sends you a DM when price crosses threshold.
* Support multiple fiat currencies (USD, EUR, GBP).
* Add inline mode or channel broadcasting.
* Persist subscriptions/alerts in a lightweight DB (SQLite / Redis).

---

## Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Open a pull request describing your changes

---

## License

This project is released under the MIT License.
