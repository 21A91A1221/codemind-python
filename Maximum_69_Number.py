def max_69(num):
    s = str(num)
    index_of_six = s.find('6')
    if index_of_six != -1:
        s=s[:index_of_six]+'9'+s[index_of_six+1:]
    r=int(s)
    return r
num=int(input())
r=max_69(num)
print(r)
