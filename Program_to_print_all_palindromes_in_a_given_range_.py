i=int(input())
j=int(input())
for n in range(i,j+1,1):
    temp=n
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if(temp==s):
        print(temp,end=" ")
