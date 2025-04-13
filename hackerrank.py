#if n add print WEIRD
n=int(input("enter a Value: "))

if (n%2==0):
#if n is even and in the inclusive range 2 to 5, print NOT WEIRD
    if (n>=2 and n<=5):
        print("not Weird")
#if n is even and in the inclusive range 6 to 20, print WEIRD
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>=20):
        print("Not Weird")
#if n is even and greater than 20, print NOT WEIRD
else:
    print("Weird")