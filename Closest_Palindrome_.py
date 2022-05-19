def palindrome(n):
    s=0
    t=n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if(t==s):
        return 1
    else:
        return 0
n=int(input())
j=n
for i in range(n-1,0,-1):
    if palindrome(i):
        break
while(j):
    j+=1
    if palindrome(j):
        break
if(j-n==n-i):
    print(i,j)
elif(j-n>n-i):
    print(i)
else:
    print(j)