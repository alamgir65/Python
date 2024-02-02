a = input()
b = input()
a = int(a)
b = int(b)
if a > b:
    print("A is greater than B")
elif a < b:
    print("B is greater than A")
else:
    print("A and B equal")

tk = input()
tk = int(tk)
if tk >= 1000:
    print("AMi kal tanggi Jamu")
    tk -= 500
    if tk >= 700:
        print("Ami chill o korbo")
    elif tk >= 550:
        print("Ice cream o khabo")
    else:
        print("direct bashai chole asbo")
elif tk >= 800:
    print("Akta jinish kinbo")
else:
    print("Sudu Programming korbo")