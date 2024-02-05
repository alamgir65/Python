n = int(input())
fibonacchi = [0]
i = 1
while i < n:
    if i == 1:
        fibonacchi.append(1)
    else:
        fibonacchi.append((fibonacchi[i-2]+fibonacchi[i-1]))
    i = i+1
    
print(*fibonacchi,sep=' ')