n,q = map(int,input().split())
s = input()
elements = s.split()
arr = [int(x) for x in elements]
pre = []
last = 0
for i,v in enumerate(arr):
    tmp = last + v
    pre.append(tmp)
    last = tmp
    
for i in range(0,q):
    l,r = map(int,input().split())
    l = l-1
    r = r-1
    ans = 0
    if l == 0:
        ans = pre[r]
    else:
        ans = pre[r]-pre[l-1]
    print(ans)