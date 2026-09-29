class Account:
    def __init__(self):
        self.accountno=int(input("account no:"))
        self.accountname=input("account name:")
        self.balance=int(input("balance:"))
    def withdraw(self):
        amount=int(input("amount to withdraw:"))
        if(amount>self.balance):
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Balance after withdraw:",self.balance)
    def deposit(self):
        amount=int(input("depositting amount:"))
        self.balance=amount+self.balance
        print("Balance after deposit:",self.balance)
    def showbalance(self):
        print("Total balance is ",self.balance)
    

l=[]
while(True):
    print("1.Create new account")
    print("2.withdraw")
    print("3.deposit")
    print("4.showbalance")
    print("5.exit")

    ch=int(input("Enter choice:"))

    if ch==1:
       a=Account()
       l.append(a)
       print(a)
    elif ch==2:
        accountno=int(input("enter account no:"))
        for i in l:
            if accountno==i.accountno:
                i.withdraw()
                break
        else:
            print("account does not exist")
    elif ch==3:
        accountno=int(input("enter account no:"))
        for i in l:
            if accountno==i.accountno:
                i.deposit()
                break
        else:
            print("account does not exist")
       
       
    elif ch==4:
        accountno=int(input("enter account no:"))
        for i in l:
            if accountno==i.accountno:
                i.showbalance()
                break
        else:
            print("account does not exist")
   
    else:
        exit()
        
