s = input().split()
n = len(s)
l = list(s)

for i in range(n):
    tmp = l[i]
    if i==n-1:
        print(tmp[::-1])
    else:
        print(tmp[::-1],end=" ")