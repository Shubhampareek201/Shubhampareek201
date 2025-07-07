d={}
while True:
    print('''\n1.Enter 1 to add phone number:-
2.Enter 2 to update phone no.:-
3.Enter 3 to remove phone no.:-
4.Enter 4 to search no. by name:-''')   

    a=int(input("\nEnter your choice="))

    if a==1:
        name=input("\nEnter the name of person:-")
        while name.isnumeric():
            name=input("\nEnter correct name:-")    
        number=input("\nEnter the number:-")
        while number.isalpha():
            number=input("Enter correct number:-") 
        while len(number)!=10:
            number=input(("\nInvalid please check the no."))
        else:
            d.update({name:number})
            print(d)
    if a==2:
        name=input("\nEnter the name of the person=")
        if name not in d:
            name=input('''NAME not in dictonary\nPlease enter correct name:-''')
        if name in d:
            number=input("Enter number:-")
            d.update({name:number})
            print(d)
         
                   
        
    if a==3:
        name=input("\nEnter the name of the person=")
        while name not in d:
            print("NOT FOUND!!!")
            name=input("Enter name again:-")
        while name in d:
            print(""+ name +" is removed\nNew dictonary is=")    
            d.pop(name)
            print(d)
    if a==4:
        name=input("\nEnter the name to search=")
        while name not in d:
            name=input("Name not found\nEnter correct name:-")
        if name in d:    
            f=d.get(name)
        print("\nNumber of the person=",f)    
    if a>4:
        print("Invalid Choice\nOne more chance")         
            
                
                