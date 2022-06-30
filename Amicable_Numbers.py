def amc(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
n=int(input())
b=int(input())
if amc(n)==b and amc(b)==n:
    print("Amicable")
else:
    print("Not Amicable")