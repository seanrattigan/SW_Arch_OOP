import random

# Q3 a
class Rectangle:
    def __init__(self, width, height, color):
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be number")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be number")
        self.width = width
        self.height = height
        self.color = color
    
    def __str__(self):
        return f"Rect {self.width} x {self.height} with col {self.color}"
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * self.width + 2 * self.height
        
rect_bucket = []
color = (100, 255, 100)
for r in range(10):
    r1 = random.randrange(5, 33)
    r2 = random.randrange(5, 33)
    rect_bucket.append(Rectangle(r1, r2, color))
#for r in rect_bucket:
#    print(r)
#    print("Area", r.area())
#    print("Perim", r.perimeter())

class Person:
    def __init__(self):
        pass

#print(type(Person()))

# Q4

class BankAccount:
    def __init__(self, customer, amount=0):
        self.name = customer
        self.balance = amount
        self.acc_number = 1000
        
    def __repr__(self):
        return f"Name:{self.name}, Balance:€{self.balance}, Acc:{self.acc_number}"
                
    def withdraw(self, amount):
        self.balance -= amount
            
    def deposit(self, amount):
        self.balance += amount
    
a = BankAccount("Ted", 298)
print(a)

class SavingsAccount(BankAccount):
    def __init__(self, customer, amount):
        if amount < 100:
            raise ValueError("Amount must be 100 or more")
        super.__init__(customer, amount)
        
    def withdraw(self, amount):
        if self.balance - amount < 80:
            print("Cannot withdraw funds- min level exceeded")
        else:
            self.balance -= amount
            
    def deposit(self, amount):
        if self.amount < 10:
            print("Min deposit is 10")
        else:
            self.balance += amount

accounts = []
for a in range(10):
    accounts.append(SavingsAccount("Ted", random.randrange(199)))
    
for acc in accounts:
    amnt = random.randrange(20)
    acc.deposit(amnt)
    print(acc)
    acc.withdraw(amnt)
    print(acc)
    print()
    acc.withdraw
