n = int(input())
# arr = []
ss = input()
elements = ss.split()
arr = [int(x) for x in elements]
arr2 = arr
# arr.reverse()
# print(arr)
arr3 = arr[::-1]
if arr2 == arr3 :
    print("YES")
else:
    print("NO")