import unittest
from utils.vpn_switcher import switch_vpn

class TestVPN(unittest.TestCase):
    def test_vpn_switch(self):
        self.assertIsNone(switch_vpn())  

if __name__ == "__main__":
    unittest.main()
