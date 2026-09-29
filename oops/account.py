class Account:
    def __init__(self):
        self.accountno=int(input("account no:"))
        self.accountname=input("account name:")
        self.balance=int(input("balance:"))
    def withdraw(self):
        amount=int(input("withdrawing amount:"))
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
        print("total balance is",self.balance)
a1=Account()
# a1.withdraw()
# a1.deposit()
# a1.showbalance()

a2=Account()
# a2.withdraw()
# a2.deposit()
# a2.showbalance()

l=[a1,a2]
for i in l:
    # print(i.accountno,i.accountname,i.balance)
    # i.withdraw()
    # i.deposit()
    # i.showbalance()
    if i.accountno==123:
        i.showbalance()
