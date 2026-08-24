import csv
import sys

def main():

    print(r"""
     __        __  _____   _        ____    ___    __  __   _____
     \ \      / / | ____| | |      / ___|  / _ \  |  \/  | | ____|
      \ \ /\ / /  |  _|   | |     | |     | | | | | |\/| | |  _|
       \ V  V /   | |___  | |___  | |___  | |_| | | |  | | | |___
        \_/\_/    |_____| |_____|  \____|  \___/  |_|  |_| |_____|
        """)
    
    csv_file = input("\nCSV file to parse: ")

    try:
        with open(csv_file, 'r') as cvfl:
            cvf = csv.DictReader(cvfl)

            overall_statistics = {
                "Total Number of Tickets": 0,
                "Total Labor Hours": 0,
                "Average Hours per Ticket": 0,
                "Shortest Ticket Duration": 50000,
                "Longest Ticket Duration": 0
            }

            tickets_by_category = {
                "Network": {"Number": 0, "Total Hours": 0, "Average Hours": 0},
                "Hardware": {"Number": 0, "Total Hours": 0, "Average Hours": 0},
                "Software": {"Number": 0, "Total Hours": 0, "Average Hours": 0},
                "Security": {"Number": 0, "Total Hours": 0, "Average Hours": 0}
            }

            tickets_by_technician = {
                "Alice": {"Tickets Handled": 0, "Total Hours": 0, "Average Hours": 0},
                "Bob": {"Tickets Handled": 0, "Total Hours": 0, "Average Hours": 0},
                "Charlie": {"Tickets Handled": 0, "Total Hours": 0, "Average Hours": 0},
                "Diana": {"Tickets Handled": 0, "Total Hours": 0, "Average Hours": 0}
            }

            tickets_by_severity = {
                "High": 0,
                "Medium": 0,
                "Low": 0,
                "Critical": 0
            }

            tickets_by_status = {
                "Open": 0,
                "Closed": 0
            }
            
            for line in cvf:
                overall_statistics["Total Number of Tickets"] += 1
                overall_statistics["Total Labor Hours"] += float(line["hours"])
                if float(line["hours"]) < overall_statistics["Shortest Ticket Duration"]:
                    overall_statistics["Shortest Ticket Duration"] = float(line["hours"])
                if float((line["hours"])) > overall_statistics["Longest Ticket Duration"]:
                    overall_statistics["Longest Ticket Duration"] = float(line["hours"])

                
                if line["category"] not in tickets_by_category:
                    tickets_by_category[line["category"]] = {
                        "Number": 1,
                        "Total Hours": float(line["hours"])
                    }
                else:
                    tickets_by_category[line["category"]]["Number"] += 1
                    tickets_by_category[line["category"]]["Total Hours"] += float(line["hours"])
                
                if line["technician"] not in tickets_by_technician:
                    tickets_by_technician[line["technician"]] = {
                        "Tickets Handled": 1,
                        "Total Hours": float(line["hours"])
                    }
                else:
                    tickets_by_technician[line["technician"]]["Tickets Handled"] += 1
                    tickets_by_technician[line["technician"]]["Total Hours"] += float(line["hours"])

                if line["priority"] not in tickets_by_severity:
                    tickets_by_severity[line["priority"]] = 1
                else:
                    tickets_by_severity[line["priority"]] += 1

                if line["status"] not in tickets_by_status:
                    tickets_by_status[line["status"]] = 1
                else:
                    tickets_by_status[line["status"]] += 1

            if overall_statistics["Total Number of Tickets"]:
                overall_statistics["Average Hours per Ticket"] = (
                    overall_statistics["Total Labor Hours"] /
                    overall_statistics["Total Number of Tickets"]
                )

            for entry in tickets_by_category:
                tickets_by_category[entry]["Average Hours"] = round(
                    tickets_by_category[entry]["Total Hours"] /
                    tickets_by_category[entry]["Number"], 2
                )

            for entry in tickets_by_technician:
                tickets_by_technician[entry]["Average Hours"] = round(
                    tickets_by_technician[entry]["Total Hours"] /
                    tickets_by_technician[entry]["Tickets Handled"], 2
                )

    except FileNotFoundError:
        print("File not found")
        sys.exit()

    print("\nSTATISTIC OVERVIEW----")
    print("Total Number of Tickets: {}\nTotal Labor Hours: {}\n"
    "Average Hours per Ticket: {}\nShortest Ticket Duration: {}\n"
    "Longest Ticket Duration: {}\n".format(overall_statistics["Total Number of Tickets"],
                                           overall_statistics["Total Labor Hours"],
                                           overall_statistics["Average Hours per Ticket"],
                                           overall_statistics["Shortest Ticket Duration"],
                                           overall_statistics["Longest Ticket Duration"])
                                           )
    
    print("\nBY CATEGORY")
    for cat in tickets_by_category:
        print("{}----".format(cat))
        print("Number: {}\nTotal Hours: {}\nAverage Hours: {}\n"
                .format(tickets_by_category[cat]["Number"],
                        tickets_by_category[cat]["Total Hours"],
                        tickets_by_category[cat]["Average Hours"])
                        )

    print("\nBY TECHNICIAN")
    for tech in tickets_by_technician:
        print("\n{}----".format(tech))
        print("Tickets Handled: {}\nTotal Hours: {}\nAverage Hours: {}\n"
                .format(tickets_by_technician[tech]["Tickets Handled"],
                        tickets_by_technician[tech]["Total Hours"],
                        tickets_by_technician[tech]["Average Hours"])
                        )

    print("\nBY SEVERITY")
    for severity in tickets_by_severity:
        print("{}: {}".format(severity, tickets_by_severity[severity]))

    print("\nBY STATUS")
    for status in tickets_by_status:
        print("{}: {}".format(status, tickets_by_status[status]))

if __name__ == '__main__':
    main()