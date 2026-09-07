from supportclasses import Employee, Developer, Manager

def main():

    emp1 = Employee("Alice", 101, 50000)
    dev1 = Developer("Bob", 102, 60000, "Python")
    mgr1 = Manager("Charlie", 103, 70000, "Sales")

    print(emp1.NAME, emp1.EMPID, emp1.salary, emp1.giveBonus())
    print(dev1.NAME, dev1.EMPID, dev1.salary, dev1.giveBonus(), dev1.describe())
    print(mgr1.NAME, mgr1.EMPID, mgr1.salary, mgr1.giveBonus(), mgr1.describe())

if __name__ == "__main__":
    main()