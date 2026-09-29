try:
    num1=int(input("num1="))
    num2=int(input("num2="))
    r=num1/num2
    print("result is",r)
except ZeroDivisionError:
    print("Zero Division error")
except ValueError:
    print('Value error')
except Exception:  #general code if any exception other than the above two occurs
    print("error")
