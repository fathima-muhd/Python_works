#ask to enter  a number..if its under 10 print too low ,if its btw 10 and 20 crct ,otherwise display too high

num=int(input('enter number:'))
if num<10:
    print("Too low")
elif num>=10 and num<=20:
    print("correct")
else:
    print('Too high')