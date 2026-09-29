#get th emark from student
#mark above 90 and less than or equal to 100 A grade
#marks above 80 and less than or equal to 90 B grade
#marks above 60 and less than or equal to 80 C grade
#below 60 fail

mark=int(input("Enter marks:"))
if mark>90:
    if mark<=100:
        print("A grade")
elif mark>80:
    if mark<=90:
        print("B grade")
elif mark>60:
    if mark<=80:
        print("C grade")
else:
    print("fail")


