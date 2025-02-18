import os
import random
from config import VPN_SERVERS

def rotate_vpn():
    selected_vpn = random.choice(VPN_SERVERS)
    os.system(f"vpn-connect {selected_vpn}")
    print(f"🔒 VPN switched to {selected_vpn}")

if __name__ == "__main__":
    rotate_vpn()
