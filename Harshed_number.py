n=int(input())
sum=0
r=0
i=n
while(i!=0):
    r=i%10
    sum=sum+r
    i=i//10
if(n%sum==0):
    print("True")
else:
    print("False")
    

