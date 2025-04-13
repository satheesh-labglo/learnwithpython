in1=str(input("enter a name"))
in2=int(input("enter your Reg number"))
class student:
    def __init__(self):#deflect use to constructor methods
        self.name=in1
        self.regno=in2
    def display(self):
        print("Name :",self.name)
        print("Reg Number :",self.regno)
        
s1=student()
s1.display()