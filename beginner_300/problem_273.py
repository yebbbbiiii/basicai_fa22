import random

class Account:
    account_count = 0
    
    def __init__(self,name,balance):
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
        
kim = Account("김민수",100)
kim1 = Account("김예빈",300)
kim.get_account_num()