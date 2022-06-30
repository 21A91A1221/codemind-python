n=int(input())
maxi=0
while n>0:
    r=n%10
    if r>maxi:
        maxi=r
    n//=10
print(maxi)