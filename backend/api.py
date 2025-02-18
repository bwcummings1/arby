from flask import Flask, jsonify, request
from db_manager import fetch_query, execute_query
from bankroll_manager import get_balance

app = Flask(__name__)

@app.route('/api/arbitrage', methods=['GET'])
def get_arbitrage_opportunities():
    results = fetch_query("SELECT * FROM arbitrage_opportunities ORDER BY timestamp DESC LIMIT 10")
    return jsonify(results)

@app.route('/api/bankroll', methods=['GET'])
def bankroll_status():
    balance = get_balance()
    return jsonify({"balance": balance})

@app.route('/api/place_bet', methods=['POST'])
def place_bet():
    data = request.get_json()
    event, stake, odds, account = data['event'], data['stake'], data['odds'], data['account']
    execute_query("INSERT INTO bets (event, stake, odds, account) VALUES (?, ?, ?, ?)", (event, stake, odds, account))
    return jsonify({"status": "bet placed"})

if __name__ == '__main__':
    app.run(debug=True)
