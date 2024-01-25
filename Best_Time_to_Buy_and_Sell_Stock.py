n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i,n):
        if c<arr[j]-arr[i]:
            c=arr[j]-arr[i]
print(c)