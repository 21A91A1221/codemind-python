n=int(input())
sum=0
sqr=n*n
while(sqr!=0):
    r=sqr%10
    sum=sum+r
    sqr=sqr//10
if(sum==n):
        print("Neon Number")
else:
    print("Not Neon Number")