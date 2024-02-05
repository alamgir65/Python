t = int(input())
def total(x,y):
    sum = 0
    for j in range(x+1,y):
        if j % 2 == 1:
            sum += j
    return sum
while t != 0:
    x , y = map(int,input().split())
    if x > y:
        tmp=x
        x=y
        y=tmp
    sum = total(x,y)
    print(sum)
    
    t -= 1