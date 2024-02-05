# If i want to use or change global variable in any function use ""global""
balance = 5000
def buy_somthing(items,price,numbers):
    global balance 
    print("Before Buying {items} the balance was : ",balance)
    balance -= (2*price)
    print("After Buying {items} the balance is : ",balance)
    
buy_somthing("Shirt",2730,2)
print("Finaly my amount is : ",balance)