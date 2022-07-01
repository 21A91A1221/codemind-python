a=input()
b=input()
c=0
if len(a)==len(b):
    for i in a:
        if i in b or i.upper() in b or i.lower() in b:
            c=1
        else:
            c=0
            break
    if c==1:
        print("True")
    else:
        print("False")
else:
    print("False")