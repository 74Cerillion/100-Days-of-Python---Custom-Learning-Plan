def readFile(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line

def formatLine(line):
    formattedOutput = dict()
    ll = line.split("|")
    timestamp = ll[0].strip()
    severity = ll[1].strip()
    hostname = ll[2].strip()
    message = ll[3].strip()
    formattedOutput["timestamp"] = timestamp
    formattedOutput["severity"] = severity
    formattedOutput["hostname"] = hostname
    formattedOutput["message"] = message
    return formattedOutput
