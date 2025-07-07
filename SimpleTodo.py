a=[]
while True:
    print(''' 1 to append
 2 to pop
 3 to remove
 4 to count
 5 to reverse''')
    c=int(input("ENter choice="))
      
    if c==1:
        b=int(input("Enter no. you wants to append="))
        a.append(b)
        print(a)
    elif c==2:
        f=int(input("Enter the index you want to remove"))
        a.pop(f)
        print(a)
    elif c==3:
        f=int(input("Enter the value you wanted to remove="))
        a.remove(f)
        print(a)
    elif c==4:
        b=int(input("Enter the no. you wants to count"))
        c=a.count(b)
        print(c)
    else:
        d=a.reverse()
        print(d)           
