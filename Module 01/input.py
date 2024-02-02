name=input("What's Your Name? : ")
age=input("How old are You? : ")
ssc_result=input("Enter Your SSC result : ")
hsc_result=input("Enter Your HSC result : ")
first_money=input("From boro vai : ")
second_money=input("From mezo vai : ")
ssc_result = float(ssc_result)
hsc_result = float(hsc_result)
first_money = int(first_money)
second_money = int(second_money)
my_total_money = first_money + second_money
total_result = ssc_result+hsc_result
text = f"My name is {name} , I am {age} years old, I got {ssc_result} in my SSC exam and {hsc_result} in my HSC exam , In last month my Elder brother give me {first_money} and my closed Elder brother give me {second_money} , Finaly my total result {total_result} and my total tk {my_total_money}"
print(text)
print(ssc_result)

