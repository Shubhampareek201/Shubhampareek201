class zoo:
    def __init__(self):
        self.name=input("Enter the name of the animal=")
        self.catagory=print("ENter the catagory of the animal")
        a=input("mamel,birds, fishes, vertibrates")
        if a=='mamel':
            zoo.mamel(self)
        elif a=='birds':
            zoo.mamel(self)
        elif a=='fishes':
            zoo.mamel(self)
        else:
            print("Invalid")            
    def mamel(self):
        a=input(f"What are the habitats of the {self.name}(carnivorous,herbivouous,omnivorous)=")
        # print("habitat is ",a)
        if a=='carnivorous':
            zoo.age(self)
        elif a=='herbivorous':
            zoo.age(self)
        elif a=='omnivorous':
            zoo.age(self)
        
    def age(self):
        a=input(f"Enter the age of the {self.name} ")       
                
                       
            
            
            
a1=zoo()
print("Name of animal=",a1.name)
print("Catagory of animal is=",a1.catagory)
# print("Habitat of the animal is=",a1.mamel())
# a1.mamel()
# print("Age of the animal is=",a1.age())

        

        

