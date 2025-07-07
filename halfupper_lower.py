a="shubhamp"
b=len(a)//2
c=''
for i in range(len(a)):
    if i>=b:
        c+=a[i].upper()
    else:
        c+=a[i]
print(c)