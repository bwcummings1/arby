from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    bets = requests.get("http://127.0.0.1:5000/api/arbitrage").json()
    return render_template('index.html', bets=bets)

@app.route('/stats')
def stats():
    bankroll = requests.get("http://127.0.0.1:5000/api/bankroll").json()
    return render_template('stats.html', bankroll=bankroll["balance"])

if __name__ == '__main__':
    app.run(debug=True)
