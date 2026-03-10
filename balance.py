class bank:
     def __init__(self,ib=0):
        self.b=ib
        
     def getbalance(self):
        print(f"current balance: {self.b}")
        
        
     def deposit(self,amount):
        if amount>0:
          self.b += amount
          print(f"deposited: {amount}")
        else:
            print("deposit amount must be posituve")
        self.getbalance()
        
     def withdraw(self,amount):
        if 0<amount<=self.b:
          self.b-=amount
          print(f"withdrawn: {amount}")
        elif amount>self.b:
            print("insufficent fund")
        else:
            print("withdrawal amount must be positive")
        self.getbalance()
        
account=bank(int(input("enter amount:")))
account.getbalance()
account.deposit(int(input("enter deposit amount:")))
account.withdraw(int(input("enter withdraw amount:")))
account.withdraw(int(input("enter withdraw amount:")))
     
