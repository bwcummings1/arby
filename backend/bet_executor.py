import random
import time
import sqlite3
from config import ACCOUNTS
from bankroll_manager import update_balance

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

def place_bet(event, stake, odds, account):
    delay = random.uniform(5, 30)  
    time.sleep(delay)
    print(f"🔒 Placing bet on {event} with ${stake} at {odds} using {account}")

    c.execute('INSERT INTO bets (event, stake, odds, account) VALUES (?, ?, ?, ?)',
              (event, stake, odds, account))
    conn.commit()
    
    # Simulate winning
    profit = stake * (odds - 1) if random.random() > 0.5 else -stake
    update_balance(account, profit)

if __name__ == "__main__":
    place_bet("Game X", 100, 2.1, "Bookie1")
