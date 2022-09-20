import random

class Account:
    account_count = 0
    
    def __init__(self,name,balance):
        self.deposit_count = 0
        
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' +num2 + '-' + num3
        
        Account.account_count +=1
    def get_account_num(self):
        print(self.account_count)
    
    def deposit(self,amount):
        if amount >=1:
            self.balance += amount
            
            self.deposit_count +=1
            if self.deposit_count % 5 ==0:
                self.balance = (self.balance * 1.01)
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
    
    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.name)
        print("계좌번호 :", self.account_number)
        print("잔고 :", self.balance)

p = Account("파이썬",10000)
p.deposit(10000)
p.deposit(20000)
p.deposit(30000)
p.deposit(40000)
p.deposit(50000)

print(p.balance)