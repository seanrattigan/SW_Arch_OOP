# @Author:srattigan
# @Date:2020-12-10 11:10:33
# @LastModifiedBy:srattigan
# @Last Modified time:2020-12-14 09:50:13
# demo class for inheritance

class BankAccount:
    """Generic Bank Account
    """
    acc_num = 100000

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_num = self.acc_num
        BankAccount.acc_num += 1

    def deposit(self, amount):
        assert amount > 0, ValueError("Must deposit a positive amount")
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        rep = f"Bankaccount for {self.name}"
        rep += f"\n\tAcc Num: {self.account_num}"
        rep += f"\n\tBalance: €{self.balance:.2f}"
        return rep

 
class SavingsAccount(BankAccount):
    """An account that pays interest
    """
    amount_limit = 400
    interest_rate = 0.02
    
    def __init__(self, name, amount):
        if amount < 50:
            raise ValueError("Account could not be created")
            return None
        super().__init__(name, amount)
    
    def withdraw(self, amount):
        if amount < self.amount_limit:
            if amount > self.balance:
                self.balance -= amount
            else:
                print("Insufficient Funds")
        else:
            print(f"Amount cannot exceed limit of {self.amount_limit}")

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


# create a student account with an overdraft allowance of €500
# each time the account goes overdrawn, there is a charge of €5 applied

if __name__ == "__main__":
    b1 = SavingsAccount("Fred Jones", 59.99)
    b2 = SavingsAccount("Myra Smith", 288.0)
    print(b1)
    print(b2)
    b1.apply_interest()
    b2.apply_interest()
    print(b1)
    print(b2)

