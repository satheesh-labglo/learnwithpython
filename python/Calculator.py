a=int(input("Enter a Frist Value:")) #user get input first value
b=int(input("Enter a Second Value:")) #user get input Secound Value
c=str(input("Enter a +, -, * and / Sysbols: ")) #which method user can used

if (c == "+"): #Addition Methods
    print("Your Addition Value is ", a+b)
elif (c == "-"): #Subraction Methods
    print("Your subtraction Value is ", a-b )
elif (c == "*"): #Multipulcation Methods
    print("Your Multipulcation Value is ", a*b )
elif (c == "/"): #Division Methods
        print("Your Division Value is ", a/b )
else:
    print(" Invalid Input" )