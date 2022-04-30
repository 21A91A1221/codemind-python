i,j=map(int,input().split())
lcm=0
if i>j:
    lcm=i
    while(lcm):
        if(lcm%i==0 and lcm%j==0):
           print(lcm)
           break
        lcm=lcm+1
else:
    lcm=j
    while(lcm):
        if(lcm%i==0 and lcm%j==0):
            print(lcm)
            break
        lcm=lcm+1