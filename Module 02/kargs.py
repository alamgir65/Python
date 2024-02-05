# This is use for more than one perameters rechive

# Simple way

def full_name(first,last,title,extra):
    name = f"I am {first} {last} I am a {title} and I'm {extra}"
    return name
name = full_name('Alamgir','Hossain','Software Engineer','Programmer')
print(name)

name2 = full_name(last="Hossain",first="Alamgir",extra="Competetive Programmer",title="Software Engineer")
print(name2)

# Its Kargs part

def fun(first,last,**Kargs):
    name = f"my name is {first} {last}"
    for key, value in Kargs.items():
        print(f"Name {key} -> {value}")
    return name

name = fun(last="Hossain",first="Alamgir",title="Engineer",crush="Fayeza",Rohan_gf="Mim")

# Return Multiple Value from Function 

def return_multiple(num1,num2):
    sum = num1 + num2
    sub = num1 - num2
    rem = num1 % num2
    return sum,sub,rem

multiple_value = return_multiple(20,3)
print(multiple_value)