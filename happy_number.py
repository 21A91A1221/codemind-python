def happy(n):
    s=0
    while (1):
        s=0
        while n>0:
            r=n%10
            s+=r**2
            n//=10
        if s<10:
            break
        else:
            n=s
            continue
    if s==1 or s==7:
        return 1
    else:
        return 0
n=int(input())
res=happy(n)
if res==1:
    print("True")
else:
    print("False")