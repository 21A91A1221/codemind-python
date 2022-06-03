n=int(input())
v=0
while n:
    r=n%10
    v+=r
    n=n//10
    if n==0 and v>10:
        n=v
        v=0
print(v)