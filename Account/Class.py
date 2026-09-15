class Account:

    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount debit successfully", amount)
            print("Remaining Balance", self.balance)
            
        else:
            print("insufficient balance")
        

    def credit(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
            
            print("Credited amount", amount)
            print("Updated balance", self.balance)
        else:
            print(" invalid amount")
            
account = Account(10000, 101)
account.credit(2000)
