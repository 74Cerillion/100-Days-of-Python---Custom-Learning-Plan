systems = [
    {"hostname": "web-01", "os": "Ubuntu", "status": "online", "cpu": 34},
    {"hostname": "db-01", "os": "RHEL", "status": "online", "cpu": 81},
    {"hostname": "dev-01", "os": "Ubuntu", "status": "offline", "cpu": 0},
    {"hostname": "win-01", "os": "Windows", "status": "online", "cpu": 67},
    {"hostname": "web-02", "os": "Ubuntu", "status": "online", "cpu": 92},
    {"hostname": "db-02", "os": "RHEL", "status": "offline", "cpu": 0},
]

#method 1: for loops
hostnames = list()
for i in systems:
    hostnames.append(i['hostname'])
print(hostnames)

lcHostnames = [i['hostname'] for i in systems]
print(lcHostnames)

operatingSystems = list()
for i in systems:
    if i['status'] == 'online':
        operatingSystems.append(i["os"])
print(operatingSystems)

lcOperatingSystems = [i['os'] for i in systems if i['status'] == 'online']
print(lcOperatingSystems)

hostnamesHighCpuUtil = list()
for i in systems:
    if i['cpu'] >= 80:
        hostnamesHighCpuUtil.append(i['hostname'])
print(hostnamesHighCpuUtil)

lcHostnamesHighCpuUtil = [i['hostname'] for i in systems if i['cpu'] >= 80]
print(lcHostnamesHighCpuUtil)

linuxSystems = list()
for i in systems:
    if i['os'] in ['Ubuntu', 'RHEL'] and i['status'] == 'online':
        linuxSystems.append(i['hostname'].upper())
print(linuxSystems)

lcLinuxSystems = [i['hostname'].upper() for i in systems if i['os'] in ['Ubuntu', 'RHEL'] and i['status'] == 'online']
print(lcLinuxSystems)

#method 2: List comprehensions put under each for loop