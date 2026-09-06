from supportClasses import Computer
from functions import createCPU, createRAM, createStorage

def main():
    print("Welcome to the Computer Configuration Program!")

    oCPU = createCPU()
    oram1 = createRAM()
    ostorage1 = createStorage()

    computer = Computer(oCPU, oram1, ostorage1)
    computer.show()

if __name__ == "__main__":
    main()