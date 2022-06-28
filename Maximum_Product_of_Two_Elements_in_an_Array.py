arr=list(map(int,input().split()))
maxi=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            prd=(arr[i]-1)*(arr[j]-1)
            if prd>maxi:
                maxi=prd
print(maxi)
                