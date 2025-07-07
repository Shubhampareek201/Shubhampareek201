class account():
    def __init__(self):
        self.balance=int(input("enter balance"))
        self.accno=int(input("enter account no"))
        
    def credit(self,amount):
        self.balance+=amount
        print("You have added",amount,"in account\n")
        print ("your balance is",self.balance)
    def debit(self,amount):
        self.balance-=amount
        print("\nYou have debited",amount,"To the balance\n")
        return("Your balance is ",self.balance)        
    def balance(self):
        return self.balance 
a1=account() 
print(a1.balance)
print(a1.accno)
a1.credit(10000)
a1.debit(20000)
print("your balance is=",a1.balance)   