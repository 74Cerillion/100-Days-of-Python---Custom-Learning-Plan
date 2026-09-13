from pathlib import Path
from supportingFunctions import readFile, formatLine

relativePath = input("Enter relative path to log file: ")

buildPath = Path(__file__).resolve().parent
absolutePath = buildPath / relativePath

stat = input("Enter Status to parse by: ")

parseLogs = readFile(absolutePath)
for line in parseLogs:
    if stat.upper() in line:
        formatted = formatLine(line)
        print(formatted)