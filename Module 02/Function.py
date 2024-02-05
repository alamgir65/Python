# This is for function in python

def double_it(num):
    return 2*num

def sum(num1,num2):
    return num1+num2

total = sum(10,32)
print("Total Sum is ",total)

final = double_it(sum(10,32))
print("Final Result : ",final)

final = double_it(final)
print("Final Result : ",final)
