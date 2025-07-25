import os
from datetime import datetime

# Fancy colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color

# Fancy ASCII art
ascii_art = r"""
  ____     _                _            _ 
 |  _ \ __| |_   _  ___ ___(_) ___  _ __| |
 | |_) / _` | | | |/ __/ __| |/ _ \| '__| |
 |  __/ (_| | |_| | (__\__ \ | (_) | |  | |
 |_|   \__,_|\__,_|\___|___/_|\___/|_|  |_|
"""

def fancy_echo():
    print(ascii_art)
    print(f"{CYAN}{'-'*45}{NC}")
    print(f"{GREEN}Hello from your repository!{NC}")
    print(f"{YELLOW}You can do anything you set your mind to.{NC}")
    print(f"{CYAN}{'-'*45}{NC}")
    print(f"{RED}Current Date and Time:{NC} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{RED}Current User:{NC} {os.getenv('USER') or os.getenv('USERNAME') or 'Unknown'}")
    print(f"{CYAN}{'-'*45}{NC}")

if __name__ == "__main__":
    fancy_echo()
