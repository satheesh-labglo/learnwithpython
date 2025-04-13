#Count the Number of Odd and Even number Between 1 to 10 and print it 

odd_count=0 
even_count=0 

for i in range (1,20):
    if (i%2 == 0): #even number 
        print(i , end=" ") #print Even number
        even_count=even_count+1 #even number count

#\n used for next line when printing output.    
print("\nTotal Even number count",even_count) #print even number count

for j in range (1,20):
    if (j%2 != 0): #odd number
        print(j, end=" ") #print odd Number
        odd_count=odd_count+1 #odd number count
        
#\n used for next line when printing output.           
print("\nTotal odd number count", odd_count) #print odd number count
