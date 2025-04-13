class laptop:
    def __init__(self):
        self.price=0
        self.processer=" "
        self.ram=", "
    def display(self):
        print("price:",self.price)
        print("processer:",self.processer)
        print("ram:",self.ram)

acer=laptop()
dell=laptop()
hp=laptop()

acer.price=55,999
acer.processer="intel core i5"
acer.ram="16GB"  

hp.price=49,999
hp.processer="intel core i3"
hp.ram="16GB"

dell.price=45,999
dell.processer="intel core i3 12th Gen"
dell.ram="8GB"

acer.display()
