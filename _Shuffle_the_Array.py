n=int(input())
arr=list(map(int,input().split()))
m=n//2
for i in range(m):
    print(arr[i],arr[m+i],end=" ")