from dataclasses import dataclass
from enum import StrEnum
from xml.parsers.expat import model

class StorageTypes(StrEnum):
    """Storage Types to support Storage Class"""
    HDD = "HDD"
    SSD = "SSD"
    NVMe = "NVMe"

class Computer:
    """Object Controller Object"""

    def __init__(self, oCPU, oRAM, oStorage):
        self._oCPU = oCPU
        self._oRAM = []
        self._oStorage = []

        self.addRAM(oRAM)
        self.addStorage(oStorage)

    @property
    def oCPU(self):
        return self._oCPU

    @oCPU.setter
    def oCPU(self, maybeCPU):
        if isinstance(maybeCPU, CPU):
            self._oCPU = maybeCPU
        else:
            raise TypeError("oCPU must be an instance of CPU class")

    @property
    def oRAM(self):
        return self._oRAM

    @oRAM.setter
    def oRAM(self, oRAM):
        if isinstance(oRAM, RAM):
            self._oRAM.append(oRAM)
        else:
            raise TypeError("oRAM must be an instance of RAM class")

    @property
    def oStorage(self):
        return self._oStorage

    @oStorage.setter
    def oStorage(self, maybeStorage):
        if isinstance(maybeStorage, Storage):
            self._oStorage.append(maybeStorage)
        else:
            raise TypeError("oStorage must be an instance of Storage class")

    @property
    def totalRAM(self):
        amtRAM = 0
        for o in self._oRAM:
            amtRAM += o.capacity
        return amtRAM

    @property
    def totalStorage(self):
        amtStorage = 0
        for o in self._oStorage:
            amtStorage += o.capacity
        return amtStorage

    def show(self):
        print(f"CPU: {self._oCPU}")
        print(f"Total RAM: {self.totalRAM} GB")
        print(f"Total Storage: {self.totalStorage} GB")

    def addRAM(self, oRAM):
        if isinstance(oRAM, RAM):
            self._oRAM.append(oRAM)
        else:
            raise TypeError("oRAM must be an instance of RAM class")

    def addStorage(self, oStorage):
        if isinstance(oStorage, Storage):
            self._oStorage.append(oStorage)
        else:
            raise TypeError("oStorage must be an instance of Storage class")

@dataclass
class CPU:
    """CPU Object"""
    make: str
    model: str
    cores: int
    clockSpeed: float  # in GHz

    def __post_init__(self):
        if self.cores <= 0:
            raise ValueError("Cores must be a positive integer")
        if self.clockSpeed <= 0:
            raise ValueError("Clock speed must be a positive float")
        if not isinstance(self.make, str) or not isinstance(self.model, str):
            raise TypeError("Make and model must be strings")
        if self.make == "" or self.model == "":
            raise ValueError("Make and model cannot be empty strings")

@dataclass
class RAM:
    """RAM Object"""
    make: str
    capacity: int  # in GB
    speed: float  # in MHz

    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        if self.speed <= 0:
            raise ValueError("Speed must be a positive float")
        if self.make == "":
            raise ValueError("Make cannot be an empty string")

@dataclass
class Storage:
    """Storage Object"""
    make: str
    capacity: int  # in GB
    storageType: StorageTypes

    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        if not isinstance(self.storageType, StorageTypes):
            raise TypeError("storageType must be an instance of StorageTypes Enum")
        if self.make == "":
            raise ValueError("Make cannot be an empty string")