x,n = map(int,input().split())
def power(x,i):
    return x**i
i = 2
sum = 0
while i <= n:
    sum += power(x,i)
    i = i+2
print(sum)