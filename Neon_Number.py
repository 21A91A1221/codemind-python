n=int(input())
sq=n**2
s=0
temp=sq
while temp>0:
    rem=temp%10
    s+=rem
    temp//=10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")