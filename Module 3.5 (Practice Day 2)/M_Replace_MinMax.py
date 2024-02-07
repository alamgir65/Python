n = int(input())
s = input()
elements = s.split()
arr = [int(x) for x in elements]
mn = min(arr)
mx = max(arr)
i=0
j=0

for index,value in enumerate(arr):
    if mn == value:
        i = index
    if mx == value:
        j = index

arr[i]=mx
arr[j]=mn

print(*arr,sep=' ')