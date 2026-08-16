import sys
from time import sleep
from dateutil import parser

def main():
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
            global logs
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
    decision = input('\nWould you like to search for something specific?')
    while decision.lower() not in ['yes', 'no']:
        decision = input('\nInvalid Input, please answer yes or no: ')

    if decision.lower() == 'no':
        sys.exit()

    if decision.lower() == 'yes':
        filter_by = input("\nWould you like to filter by date, severity, "
        "or keyword? ")
        while filter_by.lower() not in ['date', 'severity', 'keyword']:
            filter_by = input("\nInvalid input. " \
            "Please choose to filter by either date, severity, or keyword: ")

        if filter_by.lower() == 'date':
            filter_by_date(logs)
        elif filter_by.lower() == 'severity':
            filter_by_severity(logs)
        elif filter_by.lower() == 'keyword':
            filter_by_keyword(logs)

def filter_by_date(logs):
    date = input("\nEnter desired date in format 'first 3 month, 2 day'" \
    "ex. Aug 09: ")
    parsed_file = [log for log in logs if date in log]
    print(parsed_file)
    if parsed_file:
        print(parsed_file)
    else:
        print('\nNo logs found with that date.' \
        'Please rerun the program to try again')

def filter_by_severity(logs):
    severity = input("\nDisplay options: info, warning, error." \
    "What would you like to search for? ")
    while severity.lower() not in ['info', 'warning', 'error']:
        severity = input("\nInvalid input. Choose between info, warning, or error: ")
    requested_logs = [log for log in logs if severity in log]
    if requested_logs:
        print(requested_logs)
    else:
        print("\nNo logs found")

def filter_by_keyword(logs):
    keyword = input("\nWhat keyword are you looking for? ")
    requested_logs = [log for log in logs if keyword in log]
    print(requested_logs)

if __name__ == '__main__':
    main()