def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
s=0
for i in range(1,a+1):
    if prime(i)!=1 and a%i==0:
        s+=1
print(s)