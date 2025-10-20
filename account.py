#account project
class account:
    def __init__(self,balance,accountnumber):
        self.balance=balance
        self.accountnumber=accountnumber
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}.")


user =account(5000,34567890)
user.debit(5000)
user.credit(2000)

