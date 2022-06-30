import math
def auto(n):
    c=0
    while n>0:
        r=n%10
        c+=1
        n//=10
    return c
n=int(input())
s=auto(n)
sq=n*n
if sq%math.pow(10,s)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")