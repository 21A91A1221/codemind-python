n=int(input())
l=0
t=n
while n:
    l+=1
    n=n//10
n=t
v=0
while n:
    r=n%10
    v=v+pow(r,l)
    n=n//10
    l-=1
if v==t:
    print('True')
else:
    print('False')