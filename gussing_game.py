import random
place_1=['pune',"mumbai","rajasthan","kolkata","kerala","goa","gujarat","delhi","uttarakhand"]
print("!!! Hello Gamers Welcome to the Guessing Game !!!\n")

print("First you have to sellect a Place name randomly\n")

select_1=int(input("Press 1 to sellect a random place...."))

while select_1!=1:
    select_1=int(input('''Please Enter correctly=
            Press 1 to coutinue:-'''))
else:
    place=random.choice(place_1)
    print("YOu Got the place=")
turns=10
guesses=''
while turns>0:
    failed=0
    for i in place:
        if i in guesses:
            print(i)
        else:
            print("_") 
            failed+=1
    if failed==0:
        print("You Win..")
        print("The place is=",place)
        break        
    guess=input("Enter the letters=")
    guesses+=guess
    if guesses not in place:
        print("You entered wrong")
        turns-=1    
    print("You have",turns ,"turns left")
    if turns==0:
        print("You lost the game") 
        print("place is=",place)  
                    