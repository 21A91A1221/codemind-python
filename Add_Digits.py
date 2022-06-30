def add(a):
    s=0
    temp=a
    while True:
        s=0
        while temp>0:
            r=temp%10
            s+=r
            temp//=10
        if s<10:
            return s
        else:
            temp=s
            s=0
            continue
a=int(input())
res=add(a)
print(res)
        