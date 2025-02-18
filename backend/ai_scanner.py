import requests
import json
import sqlite3
import time

# Load sportsbook APIs from config
from config import BOOKMAKERS

# Initialize database
conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS arbitrage_opportunities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT,
        odds_1 REAL,
        odds_2 REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def fetch_odds():
    odds_data = {}
    for name, url in BOOKMAKERS.items():
        try:
            response = requests.get(url)
            data = response.json()
            odds_data[name] = data
        except Exception as e:
            print(f"Error fetching odds from {name}: {e}")
    return odds_data

def detect_arbitrage(odds_data):
    arbitrage_opportunities = []
    for event in odds_data["Bookie1"]:
        if event in odds_data["Bookie2"]:
            odds_1 = odds_data["Bookie1"][event]['odds']
            odds_2 = odds_data["Bookie2"][event]['odds']
            if (1/odds_1 + 1/odds_2) < 1:
                arbitrage_opportunities.append((event, odds_1, odds_2))

                # Save to database
                c.execute('INSERT INTO arbitrage_opportunities (event, odds_1, odds_2) VALUES (?, ?, ?)',
                          (event, odds_1, odds_2))
                conn.commit()

    return arbitrage_opportunities

while True:
    odds = fetch_odds()
    arbs = detect_arbitrage(odds)
    if arbs:
        print(f"🔥 Arbitrage found: {arbs}")
    time.sleep(5)
