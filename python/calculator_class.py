class student: #we can used constructor methods
    def __init__(self,Name,Reg):
        self.name=Name
        self.regno=Reg
    def display(self):
        print("your Name is :", self.name)
        print('your register Number is :', self.regno)
    
exam = student("Frist Mid Term","100%")
exam.display()
