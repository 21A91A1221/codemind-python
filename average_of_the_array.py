n=int(input())
s=0
a=list(map(float,input().split()))
for i in a:
    s+=i
d=s/n;
print("%0.2f"%d)