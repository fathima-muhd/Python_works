#Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

while True:
    try: 
        print("1.Addition")
        print("2.Substraction")
        print("3.Mupltiplication")
        print("4.Division")
        ch=int(input("Enter The  Choice: "))
    except ValueError:
            print("Value Error")
    except:
            print("Error")  
    else: 
        if ch==1:
            try:
                num1=int(input("Enter number: "))
                num2=int(input("Enter number: "))
                print("Sum: ",num1+num2)
            except ValueError:
                 print("value error")
        elif ch==2:
            try:
                num1=int(input("Enter number: "))
                num2=int(input("Enter number: "))
                print("Substract: ",num1-num2)
            except ValueError:
                print("value error")

        elif ch==3:
            try:
                num1=int(input("Enter number: "))
                num2=int(input("Enter number: "))
                print("Multiplication:",num1*num2)
            except ValueError:
                print("value error")
            

        elif ch==4:
            try: 
                num1=int(input("Enter number: "))
                num2=int(input("Enter number: "))
                print("Division: ",num1/num2)
            except ZeroDivisionError:
                print("Zero Division Error")

        elif ch==5:
                exit()
  