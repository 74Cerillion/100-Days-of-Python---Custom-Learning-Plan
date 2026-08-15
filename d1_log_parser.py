import sys
from time import sleep

print(r"""
__      __      __  ____    _        ____    ___    _    _   _____ 
\ \    /  \    / / |  __|  | |      / ___|  / _ \  |  \/  | |  ___|
 \ \  / /\ \  / /  | |__   | |     | |     | | | | | |\/| | | |__  
  \ \/ /  \ \/ /   |  __|  | |     | |     | | | | | |  | | |  __| 
   \  /    \  /    | |__   | |___  | |___  | |_| | | |  | | | |___ 
    \/      \/     |____|  |_____|  \____|  \___/  |_|  |_| |_____|

""")

infile = input("Please input the complete filepath to the log: ")

total_by_cat = {'INFO': 0,
                'WARNING': 0,
                'ERROR': 0
                }
total = 0

try:
    with open(infile, encoding='utf-8', errors='ignore') as f:
        logs = f.readlines()

        for log in logs:
            if 'ERROR' in log:
                total_by_cat['ERROR'] += 1
            elif 'WARNING' in log:
                total_by_cat['WARNING'] += 1
            elif 'INFO' in log:
                total_by_cat['INFO'] += 1
            total += 1
except FileNotFoundError:
    print("Incorrect filepath, exiting program. Please rerun and try again.")
    sleep(1)
    sys.exit()

print("Total log files parsed = {}".format(total))
print("\nTotal Info Logs: {}\n".format(total_by_cat['INFO']))
print("\nTotal Warning Logs: {}\n".format(total_by_cat['WARNING']))
print("\nTotal Error Logs: {}\n".format(total_by_cat['ERROR']))