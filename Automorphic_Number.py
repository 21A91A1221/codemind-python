n=int(input())
t=n
l=0
while(n>0):
    l+=1
    n=n//10
n=t*t
n=n%(pow(10,l))
if(t==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')