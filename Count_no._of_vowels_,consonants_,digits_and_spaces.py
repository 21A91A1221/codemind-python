s=input()
v=c=d=w=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v=v+1
    elif((i>='a' and i<='z')or(i>='A' and i<='Z')):
        c=c+1
    elif(i.isdigit()):
        d=d+1
    elif(i==' '):
        w=w+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
    