#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsuffientBalanceError(Exception):
    pass
amount=int(input("amount="))
balance=int(input("balance="))
try:
    if balance<amount:
        raise InsuffientBalanceError("Not Enough balance.Transaction failed")
except InsuffientBalanceError as e:
    print(e)
else:
    print("Transaction successful.current balance is",balance-amount)
