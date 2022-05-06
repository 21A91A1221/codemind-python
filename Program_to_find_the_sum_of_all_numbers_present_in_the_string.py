s=input()
sum=0
for i in range(0,len(s)):
    if (ord(s[i])>=48 and ord(s[i])<=57):
        sum=sum+int(s[i])
print(sum)