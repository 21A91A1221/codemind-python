n=int(input())
lar=0
while(n>0):
    r=n%10
    if(lar<r):
        lar=r
    n=n//10
print(lar)