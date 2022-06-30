def rev(n):
    s=0
    while n>0:
        r=n%10
        s=(s*10)+r
        n//=10
    return s
n=int(input())
c=0
if n<0:
    c=1
    n*=-1
res=rev(n)
if c==1:
    print(res*-1)
else:
    print(res)