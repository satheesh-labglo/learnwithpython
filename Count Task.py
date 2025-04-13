#Count the number Which are Diviable by 3 and 5, range 1-100.
count = 0
print("Numbers divisible by both 3 and 5:")

for i in range (1,101):
    if ( i%2 == 0 and i%5 == 0):
        print(i, end=" ")   # Print numbers in the same line
        count=count+1 #Count Showing
    
#\n used for next line when printing output.    
print("\nTotal Count ", count) #print the total count and used for \n.