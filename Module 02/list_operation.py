arr = [12,7,98,34,12,56,12,56,14,56,14,14,90,78]
print(arr[:])

# append element in back of the list
# arr.append(100)
# print(arr[:])

# insert element at any position 
# list.insert(index,value)
# arr.insert(0,333) 
# print(arr[:])

# remove any element from the list 
# list.remove(value)
# arr.remove(12)
# print(arr[:])
# if any element no such this list 
if 1000 in arr:
    arr.remove(1000)

# remove the specific position
# arr.pop(0)
# print(arr[:])

# its used for remove all element from the list
# arr.clear()
# print(arr[:])

# reverse the list
arr.reverse()
print(arr[:])

#its used for sort the list
# arr.sort()
# print(arr[:])

#count any element of the list
print(arr.count(56))

# arr.index(78)
print(arr.index(1000))