class employee:
    def __init__(self,e_name,e_id,e_sal,e_no):
        self.e_name=e_name
        self.e_id=e_id
        self.e_sal=e_sal
        self.e_no=e_no
    def search(employees):
        a=input("Enter the name of the employee=")
        result=[employee for employee in employees if a in employee.e_name]
        if result:
            for a1 in result:
                print(a1.e_id,a1.e_name,a1.e_no,a1.e_sal)
        else:
            print("Not in entries")     
                         
a1=employee('shub',121,100000,9358262430)
a2=employee('Raj',122,50000,9413097615)
a3=employee('Ronit',123,50000,9413668854)
a4=employee('Maheep',124,70000,9413010547)
a5=employee('Senti',125,75000,9460696351)

a=employee
list=[a1,a2,a3,a4,a5]
a.search(list)
