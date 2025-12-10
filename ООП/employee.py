class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_paid(self):
        print(f"{self.name} получает зарплату {self.salary} руб")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_paid(self):
        total = self.salary + self.bonus
        print(f"{self.name} получает зарплату {self.salary} + бонус {self.bonus} = {total} рублей")

class Worker(Employee):
    def __init__(self, name, work_hour, hourly_rate):
        self.work_hour = work_hour
        self.hourly_rate = hourly_rate
        super().__init__(name, self.work_hour * self.hourly_rate)

    def get_paid(self):
        print(f"{self.name} получает зарплату {self.work_hour} часов * {self.hourly_rate} руб/час = {self.salary} рублей")

# сотрудники
manager = Manager("Иван", 50000, 10000)
worker = Worker("Петр", 160, 500)

manager.get_paid()
worker.get_paid()

#полиморфизм
print("\n---полиморфизм---")
employees = [manager, worker]

for employee in employees:
    employee.get_paid()