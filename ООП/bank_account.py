class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def top_up(self, summa):
        self.balance += summa
        print(f"вы пополнили счет на {summa}, ваш баланс = {self.balance}")

    def withdraw(self, summa):
        if summa <= self.balance:
            self.balance -= summa
            print(f"со счета списанно {summa} руб, ваш баланс = {self.balance}")
        else:
            print("недостаточно средств")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, percentage_of_income=5.0):
        super().__init__(account_number, balance)
        if percentage_of_income > 0:
            self.percentage_of_income = percentage_of_income
        else:
            self.percentage_of_income = 0

    def accrue_interest(self):
        share = self.balance * (self.percentage_of_income / 100)
        self.balance += share
        print(f"начислены проценты: {share} руб, новый баланс {self.balance}")

class CreditAccount(BankAccount):
    def __init__(self, account_number, balance=0, credit_limit=1232):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    def withdraw(self, summa):
        if summa > self.balance + self.credit_limit:
            print(f"нельзя снять {summa} руб, максимум {self.balance + self.credit_limit} руб")
        else:
            self.balance -= summa
            print(f"вы обеднели на {summa} руб, ваш баланс {self.balance} руб")



print("---базовый счет---")
account = BankAccount("217", 1200000)
account.top_up(400)
account.withdraw(200)

print("---сберегательный счет---")
savings = SavingsAccount("121312", 1000, 20)
savings.accrue_interest()
savings.top_up(200)
savings.withdraw(10)

print("---кредитный счет---")
credit = CreditAccount("88712", 4000, 10000)
credit.top_up(1200)
credit.withdraw(5400)
credit.withdraw(9800)
credit.withdraw(0)
