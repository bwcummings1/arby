def calculate_stakes(bankroll, odds_1, odds_2):
    stake_1 = bankroll * (odds_2 / (odds_1 + odds_2))
    stake_2 = bankroll * (odds_1 / (odds_1 + odds_2))
    return round(stake_1, 2), round(stake_2, 2)

def expected_profit(stake_1, odds_1, stake_2, odds_2):
    return max(stake_1 * (odds_1 - 1) - stake_2, stake_2 * (odds_2 - 1) - stake_1)

if __name__ == "__main__":
    bankroll = 1000
    stake_1, stake_2 = calculate_stakes(bankroll, 2.1, 1.9)
    profit = expected_profit(stake_1, 2.1, stake_2, 1.9)
    print(f"Stakes: ${stake_1} & ${stake_2}, Expected Profit: ${profit}")
