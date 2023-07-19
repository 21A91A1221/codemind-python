for i in range(int(input())):
    i=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in l:
        c+=(j%2);
    print(c//2)