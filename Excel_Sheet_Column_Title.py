n=int(input())
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
st=""
while n>0:
    r=n%26
    if r==0:
        s+='Z'
        n=(n//26)-1
    else:
        st+=alpha[r-1]
        n=(n//26)
for i in range(len(st)-1,-1,-1):
    print(st[i],end="")