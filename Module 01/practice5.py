# Grade Calculator 
subject_number = input("Enter Your Subject Number : ")
subject_number = int(subject_number)
sum = 0
flag = True
n = subject_number
while subject_number > 0 :
    marks = input("Enter Your marks : ")
    marks = int(marks)
    if marks >= 80:
        sum += 5.0
    elif marks >= 70:
        sum += 4.0
    elif marks >= 60:
        sum += 3.5
    elif marks >= 50:
        sum += 3.0
    elif marks >= 40:
        sum += 2.0
    elif marks >= 33:
        sum += 1.0
    else:
        flag=False
    subject_number -= 1
grade = sum/n
if flag is not True:
    print("You are Fail in Your exam")
else:
    print(f"You got {grade}")