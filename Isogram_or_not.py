def is_isogram(s):
    s=s.lower()
    char_set=set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True
s=input()
r=is_isogram(s)
print(r)