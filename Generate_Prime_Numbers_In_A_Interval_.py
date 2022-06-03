v=int(input())
k=int(input())
for i in range(v,k+1,1):
    a=0
    for j in range(1,i+1,1):
        if i%j==0:
            a+=1
    if a==2:
        print(i)