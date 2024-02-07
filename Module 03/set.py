# set is a list that exist only unique element , and is does not exist index because its keep value randomly
arr = [17,125,1,3,4,1,35,4,3,2,67]
print(arr)

st = set(arr)
print(st)

stt = {2,3,5,3,5,8,9,10,22,3}
print(stt)

stt.add(12)
stt.add(27)
stt.add(12)
stt.add(13)
print(stt)

stt.remove(27)
stt.remove(2)
print(stt)

# for item in stt:
#     print(item)
    
if 13 in stt:
    print("13 is exist")
elif 27 not in stt:
    print("27 does not exist")
    
print(len(stt))


st1 = {5,27,1,2,4,2,4,234,53,1,5,3,56}
st2 ={322,131,1,2,35,3,68}

print(st1 & st2) #this is set intersection operation
print(st1 | st2) # this is union operation
# print(st1 & st2)