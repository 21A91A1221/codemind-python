n=int(input())
v=0
k=1
r=0
for i in range(1,n+1,1):
    print(v,end=' ')
    r=v+k
    v=k
    k=r