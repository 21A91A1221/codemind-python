n=int(input())
s=0
for i in range(1,n,1):
    r=n%i
    if(r==0):
        s=s+i
if(s==n):
    print(True)
else:
    print(False)