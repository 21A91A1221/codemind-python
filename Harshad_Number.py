def harshad(num):
    digits = [int(digit) for digit in str(num)]
    s=sum(digits)
    return num%s==0
t=int(input())
for i in range(t):
    num=int(input())
    if harshad(num):
        print("YES")
    else:
        print("NO")