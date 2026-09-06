from supportClasses import StorageTypes, CPU, RAM, Storage

def createCPU():
    print("Creating CPU...")
    make = input("Enter CPU make: ")
    model = input("Enter CPU model: ")
    cores = int(input("Enter number of cores: "))
    clockSpeed = float(input("Enter clock speed (in GHz): "))

    return CPU(make, model, cores, clockSpeed)

def createRAM():
    print("Creating RAM...")
    make = input("Enter RAM make: ")
    capacity = int(input("Enter RAM capacity (in GB): "))
    speed = float(input("Enter RAM speed (e.g., 3200 MHz, 3600 MHz): "))

    return RAM(make, capacity, speed)

def createStorage():
    print("Creating Storage...")
    make = input("Enter Storage make: ")
    capacity = int(input("Enter Storage capacity (in GB): "))
    storageTypeInput = input("Enter Storage type (HDD, SSD, NVMe) [CASE SENSITIVE]: ")

    try:
        storageType = StorageTypes[storageTypeInput]
    except KeyError:
        raise ValueError(f"Invalid storage type: {storageTypeInput}. Must be one of {list(StorageTypes)}")

    return Storage(make, capacity, storageType)