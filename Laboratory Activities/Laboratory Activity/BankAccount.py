from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def _update_balance(self, new_balance):
        self.__balance = new_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._update_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self._update_balance(self.balance - amount)
        else:
            print("Overdraft limit exceeded!\n")

    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._update_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self._update_balance(self.balance - amount)
        else:
            print("Insufficient balance! No overdraft allowed.")

    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("-" * 30)

s1 = SavingsAccount("SA123", 1000)
s2 = SavingsAccount("SA124", 1500)
c1 = CurrentAccount("CA123", 500)
c2 = CurrentAccount("CA124", 0)


s1.deposit(300)
s1.withdraw(100)

s2.withdraw(1600)  

c1.withdraw(5200)  
c2.withdraw(6000) 


accounts = [s1, s2, c1, c2]
for acc in accounts:
    print_account_details(acc)