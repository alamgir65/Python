# def fun(a,b,*c):
#     sum=a+b
#     for i in c:
#         sum += i
#     return sum

# sum = fun(2,4,6,8,10,12,14)
# print(sum)

def fun(name,roll,gpa,**extra):
    for key,i in extra.items():
        print(key,"---> ",i)
    return f"Your name is {name} , your Class roll is {roll} , Your HSC result {gpa}"
full = fun(name="Alamgir Hossain",roll=131,gpa=5.00,crush="Kashfia Chowdhury",ex="Sathi")
print(full)


def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")