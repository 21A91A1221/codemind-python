def rev(n):
    s=0
    while n>0:
        rem=n%10
        s=(s*10)+rem
        n//=10
    return s
n=int(input())
arev=rev(n)
if n**2==rev(arev**2):
    print("True")
else:
    print("False")