Salary=int(input("salary eligible above 20000: "))
age=int(input("enter your Age limit 25 only: "))

if (Salary >= 20000 or age <= 25):
    loan=int(input("enter a Loan Amount: "))
    if loan > 50000:
        print("Maximum loan amount is 50000 only ")
    else:
        print("Yeah i Will Give the Amount")
else:
    print("You are Not Selected")