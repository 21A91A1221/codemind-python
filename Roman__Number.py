def int_to_roman(num):
    roman_nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    for val, nm in roman_nums:
        while num>=val:
            result+=nm
            num-=val
    return result
num=int(input())
print(int_to_roman(num))