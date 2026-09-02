from dataclasses import dataclass, field

@dataclass
class Switch:
    hostname: str = field(default="localhost")
    port: int = field(default=8080)
    maxConnections: int = field(default=10)
    vlans: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.hostname:
            raise ValueError("Invalid Input, Expected truthy str.")
        if not (0 < self.port < 65535):
            raise ValueError("Invalid Port, Expected digit between 0-65535.")
        if not (0 < self.maxConnections):
            raise ValueError("Invalid input, Expected positive int")

    def change_hostname(self, new_hostname: str):
        if not new_hostname:
            raise ValueError("Invalid Input, Expected truthy str.")
        self.hostname = new_hostname

normalConstruction = Switch('s1', 443, 3, ['vlan1', 'vlan2'])
defaultConstruction = Switch()

try:
    rejectedConstruction = Switch('', 70000, -1, [])
except ValueError as e:
    print(f"Rejected construction: {e}")

print(normalConstruction == defaultConstruction)
print(normalConstruction)
print(defaultConstruction)