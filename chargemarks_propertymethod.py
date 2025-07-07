class student():
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
        self.percentage=str((self.chem+self.math+self.phy)/3)+" %"
    @property     
    def per(self):
        per=str((self.chem+self.math+self.phy)/3)+" %"
        return per
            
a=student(95,96,88)
print(a.percentage)

a.math=80
print(a.per)