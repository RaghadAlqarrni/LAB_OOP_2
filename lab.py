from classes import BankAccount

try:
        account1 = BankAccount("Raghad", 500)
        account2 = BankAccount("Majd", 100)  

        print(account1.get_account_holder())  
        print(account2.get_account_holder())  

        account1.deposit(5000)
        account2.deposit(100)
       
        account1.withdraw(300)

        print(f"Balance after withdrawing $300 from account1: {account1.get_balance()}") 
        print(f"Balance from account2: {account2.get_balance()}")  
except Exception as e:
        print(e)