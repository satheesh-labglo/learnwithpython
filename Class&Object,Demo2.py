class teacher:
    def __init__(self,Name,Reg):
        self.name=Name
        self.regno=Reg
    def display(self):
        print("Name:", self.name)
        print("Reg number : ",self.regno)
 
t1=teacher("satheesh","21")
t2=teacher("kumar","784515")      

t1.display()
t2.display()  