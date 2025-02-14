class BankAccount:
    def __init__(self, account_holder: str, initial_balance=0):
        self.__account_holder = account_holder
        self.__balance = 0 
        if initial_balance < 0:
            raise ValueError("Initial balance must be 0 or positive.")
        self.deposit(initial_balance) 

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount 
            return self.__balance 
        elif amount >= 0:
            print("Deposit amount must be positive!.")
        else:
            raise Exception("error") 
            

    def withdraw(self, amount: int):
        if amount > self.__balance:
            raise Exception("Not enough funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder