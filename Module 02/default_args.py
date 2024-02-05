# This video for args ,

def total_sum(num1, num2,num3=0,num4=0):
    return num1 + num2 + num3 + num4

total = total_sum(23,22,45)
print("Total : ",total)

# Args

def all_sum(num1 , num2, *args):
    print("This is Args : ",args)
    sum = 0
    for num in args:
        sum += num
        print(num)
    return sum

final = all_sum(2,7,90,32,5,90,1,2,4)
print("The all Sum is ",final)