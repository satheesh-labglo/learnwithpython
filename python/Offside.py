rows=int(input("enter a Number"))
for i in range(0,rows):
    for j in range(0,i):
        print(i,end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(0,i):
        print(i, end=" ")
    print()
