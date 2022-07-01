a=input()
a2=""
res=""
for i in a:
    if i.isupper():
        a2+=i.lower()
    else:
        a2+=i
arr=list(a2.split())
for i in arr:
    for j in i:
        c=0
        for k in arr:
            if j in k:
                c=1
            else:
                c=0
                break
        if c==1:
            res+=j
    break
if len(res)==0:
    print(0)
else:
    print(len(res))