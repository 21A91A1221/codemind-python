a=int(input())
n=0
s=1
c=0
for i in range(a):
    print(n,end=" ")
    c=n+s
    n=s
    s=c