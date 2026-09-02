from dataclasses import dataclass, field

#define object type
@dataclass
class Switch: #attributes automatically defined on instantiation
    hostname: str = field(default="localhost")#includes type hints
    port: int = field(default=8080)
    maxConnections: int = field(default=10)
    vlans: list[str] = field(default_factory=list) #mutable

    def __post_init__(self): #validate after __init__ is called
        if not self.hostname:
            raise ValueError("Invalid Input, Expected truthy str.")
        if not (0 < self.port < 65535):
            raise ValueError("Invalid Port, Expected digit between 0-65535.")
        if not (0 < self.maxConnections):
            raise ValueError("Invalid input, Expected positive int")

    #option to change hostname after instantiation
    #the other attributes would work the same way, since this is academic,
    #we will only implement this for hostname
    def change_hostname(self, new_hostname: str):
        if not new_hostname:
            raise ValueError("Invalid Input, Expected truthy str.")
        self.hostname = new_hostname

#define an object normally
normalConstruction = Switch('s1', 443, 3, ['vlan1', 'vlan2'])
#define an object with defaults
defaultConstruction = Switch()

#intentionally define an object with invalid inputs to demonstrate validation
#handle the error gracefully with try/except
try:
    rejectedConstruction = Switch('', 70000, -1, [])
except ValueError as e:
    print(f"Rejected construction: {e}")

#demonstrate that the two objects are not equal
print(normalConstruction == defaultConstruction)

#demonstrate that default_factory gives a new list for each instance
print(normalConstruction)
print(defaultConstruction)