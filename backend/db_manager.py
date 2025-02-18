import sqlite3

DB_FILE = "db.sqlite"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Table for tracking arbitrage opportunities
    c.execute('''
        CREATE TABLE IF NOT EXISTS arbitrage_opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            odds_1 REAL,
            odds_2 REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Table for tracking executed bets
    c.execute('''
        CREATE TABLE IF NOT EXISTS bets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            stake REAL,
            odds REAL,
            account TEXT,
            outcome TEXT DEFAULT 'pending',
            profit REAL DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Table for user management (multi-user support)
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            balance REAL DEFAULT 1000.0
        )
    ''')

    conn.commit()
    conn.close()

def execute_query(query, params=()):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(query, params)
    result = c.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized successfully.")
