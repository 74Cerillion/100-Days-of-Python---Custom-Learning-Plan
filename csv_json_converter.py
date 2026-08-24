import csv
import json
from pathlib import Path

file = input("Enter file to convert: ")
conversion = input("Convert from json -> csv (1) or csv -> json (2): ")

while True:
    file = Path(file)
    if file.exists():
        break
    else:
        file = input("Invalid Filepath, please enter valid path: ")

while True:
    if conversion == "1" or conversion == "2":
        break
    else:
        conversion = input("Invalid Decision, " \
        "choose 1 for csv -> json or 2 for json -> csv")

#Input is collected and validated at this point, proceed with logic
if conversion == "1":
    with open(file, 'r') as f:
        data = json.load(f)
        print(data)
        out = data["technicianS"]

    with open('sample.csv', 'w', newline='') as dn:
        fieldnames = out[0].keys()
        writer = csv.DictWriter(dn, fieldnames=fieldnames)
        writer.writeheader()
        for entry in out:
            writer.writerow(entry)

if conversion == "2":
    with open(file, 'r') as f:
        ccontent = csv.reader(f)
        next(ccontent)
        data = {"technicianS": []}
        for row in ccontent:
            data["technicianS"].append({
                "Name": row[0],
                "Role": row[1],
                "Skill": row[2]
            })

    with open("sample.json", 'w') as f:
        json.dump(data, f, indent=4)