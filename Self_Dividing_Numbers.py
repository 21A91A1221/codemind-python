def sd(r):
    a=b=0
    t=r
    while(r):
        d=r%10
        if d==0:
            return 0
        if t%d==0:
            b+=1
        a+=1
        r=r//10
    if a==b:
        return 1
    else:
        return 0
v=int(input())
k=int(input())
for r in range(v,k+1):
    if(sd(r)):
        print(r,end=' ')