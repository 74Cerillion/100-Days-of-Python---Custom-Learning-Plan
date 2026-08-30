class Switch:

    def __init__(self, hostname=str, port=int, maxConnections=int):
        self._hostname = hostname
        self._port = port
        self._maxConnections = maxConnections

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, newHostname):
        if len(newHostname) > 0:
            self._hostname = newHostname
        else:
            raise ValueError("Invalid Input, Expected truthy str.")

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, newPort):
        if 0 < newPort < 65535:
            self._port = newPort
        else:
            raise ValueError("Invalid Port, Expected digit between 0-65535.")
    
    @property
    def maxConnections(self):
        return self._maxConnections

    @maxConnections.setter
    def maxConnections(self, newMc):
        if 0 < newMc:
            self._maxConnections = newMc
        else:
            raise ValueError("Invalid input, Expected positive int")

def main():

    s1 = Switch('s1', 443, 3)

    print("SERVER CONFIGURATION")

    print(s1._hostname)
    print(s1._port)
    print(s1._maxConnections)

    print("Updating switch configuration...")

    s1.port = 2
    print(s1.port)
    s1.hostname = 's2'
    print(s1.hostname)
    s1.maxConnections = 4
    print(s1.maxConnections)

if __name__ == '__main__':
    main()