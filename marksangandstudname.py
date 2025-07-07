class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod    
    def hello():
        print("hello world")    
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
            a=sum/3
        print("Hey",self.name,"Your average marks is",a)    
        
        
s1=student("Shubham",[90,80,60])
print(s1.name,s1.marks)
s1.hello() 
s1.get_avg()