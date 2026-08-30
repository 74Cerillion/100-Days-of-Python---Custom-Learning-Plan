class Switch:

    #init instance attributes
    def __init__(self, hostname=str, port=int, maxConnections=int): #<%2#>
        self._hostname = hostname #<%9#>
        self._port = port
        self._maxConnections = maxConnections

    #prpoperty catcher for hostname
    #when an object is instantiated, catches the hostname before it goes into the self._hostname attr
    @property
    def hostname(self): #<%3#>
        return self._hostname #<%8#>

    #setter object for hostname
    #catches the hostname from the hostname property for validation and writing, then sets equivalency
    @hostname.setter #<%4#>
    def hostname(self, newHostname): #<%5#>
        if len(newHostname) > 0: #<%6#>
            self._hostname = newHostname #<%7#>
        else:
            raise ValueError("Invalid Input, Expected truthy str.")

    #property for port
    @property
    def port(self):
        return self._port

    #setter object and validation logic for port
    @port.setter
    def port(self, newPort):
        if 0 < newPort < 65535:
            self._port = newPort
        else:
            raise ValueError("Invalid Port, Expected digit between 0-65535.")

    #property for maxConnections
    @property
    def maxConnections(self):
        return self._maxConnections

    #setter obect and validation logic for maxConnections
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

    #Note, able to access attr normally, but able to call it through its property
    #To follow data stream - Track the <%%##> tags I've laid throughout the whole document
    #I wish I had somebody show me the flow of data when I was learning this
    #You can think of those as 'touch tags'. Every place with a tag is a place where that
    #piece of data 'touches' on its way through the program/process/calculations
    s1.port = 2
    print(s1.port)
    s1.hostname = 's2' #<%1#>
    print(s1.hostname) #<%10#>
    s1.maxConnections = 4
    print(s1.maxConnections)

if __name__ == '__main__':
    main()