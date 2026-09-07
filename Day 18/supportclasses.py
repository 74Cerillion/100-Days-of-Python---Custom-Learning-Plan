from dataclasses import dataclass

@dataclass
class Employee:
    NAME: str
    EMPID: int
    salary: float

    def giveBonus(self):
        return self.salary * 0.05

class Developer(Employee):

    def __init__(self, NAME, EMPID, salary, language):
        super().__init__(NAME, EMPID, salary)
        self.language = language

    def giveBonus(self):
        return self.salary * 0.10

    def describe(self):
        return f"{self.NAME} is a developer who codes in {self.language}."

class Manager(Employee):

    def __init__(self, NAME, EMPID, salary, dept):
        super().__init__(NAME, EMPID, salary)
        self.dept = dept

    def giveBonus(self):
        return self.salary * 0.15

    def describe(self):
        return f"{self.NAME} is a manager in the {self.dept} department."