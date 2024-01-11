def squares(num):
    for i in range(int(num**0.5) + 1):
        for j in range(i, int(num**0.5) + 1):
            if i**2 + j**2 == num and i != j:
                return True
    return False
num=int(input())
r=squares(num)
print(r)