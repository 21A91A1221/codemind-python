t=int(input())
arr=list(map(int,input().split()))
arr.sort()
l=[]
for i in arr:
    if i not in l:
        l.append(i)
if len(l)<3:
    print(max(l))
else:
    print(l[len(l)-3])