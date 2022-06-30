u=input()
n=s=0
for i in u:
    n=0
    for j in u:
        if i==j:
            n+=1
    if n==1:
        s=1
    else:
        s=0
        break
if s==1:
    print("Unique Number")
else:
    print("Not Unique Number")