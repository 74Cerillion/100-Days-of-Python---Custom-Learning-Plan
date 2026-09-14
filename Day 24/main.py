events = [
    {"host": "web-01", "severity": 3, "events": 17},
    {"host": "db-02", "severity": 5, "events": 4},
    {"host": "auth-01", "severity": 4, "events": 29},
    {"host": "web-03", "severity": 2, "events": 41},
    {"host": "db-01", "severity": 5, "events": 12},
    {"host": "auth-02", "severity": 1, "events": 8},
]

#1
req1 = sorted(events, key=lambda event: event['host'])
print(req1)

#2
req2 = sorted(events, key=lambda event: event['severity'], reverse=True)
print(req2)

#3
req3 = max(events, key=lambda event: event['events'])
print(req3)

#4
req4 = sorted(
    events, key=lambda event: (-event['severity'], -event['events'])
)

#Part 2
def getSeverity(event):
    return event["severity"]
print(sorted(events, key=getSeverity))

print(sorted(events, 
             key=lambda event: event["severity"]
             ))