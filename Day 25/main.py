servers = ["web-01", "db-01", "auth-01", "backup-01"]

cpu_usage = [42, 91, 67, 28]

services_running = [True, True, False, True]

report = list()

for server, cpu, service in zip(servers, cpu_usage, services_running):
    report.append({
        "server": server,
        "cpu": cpu,
        "service": service
    })
print(report)

for ndx, i in enumerate(report, start=1):
    print(ndx, i)

if any(i['cpu'] > 85 for i in report):
    print(True)
if not all(i['service'] == True for i in report):
    print(False)