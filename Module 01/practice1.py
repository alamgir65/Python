num1 = input("Enter 1st Number : ")
num2 = input("Enter 2nd Number : ")
num3 = input("Enter 3rd Number : ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
mx = num1
if num2 > num1 and num2 > num3:
    mx=num2
else:
    mx=num3
print("maximum Number: ",mx)