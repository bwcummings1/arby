import unittest
from backend.ai_scanner import detect_arbitrage

class TestArbitrageScanner(unittest.TestCase):
    def test_arbitrage_detection(self):
        odds_data = {
            "Bookie1": {"Game A": {"odds": 2.1}},
            "Bookie2": {"Game A": {"odds": 1.9}}
        }
        result = detect_arbitrage(odds_data)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
