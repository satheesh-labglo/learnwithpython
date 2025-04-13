#gave input 10 numbers from keyboard and find their sum and average using Python program
# Initialize sum variable
total_sum = 0

# Take 10 numbers as input from the user
print("Enter 10 numbers:")
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))  # Taking input as float to handle decimal numbers
    #total_sum += num  # Adding the number to sum
    total_sum=total_sum + num

# Calculate average
average = total_sum / 10


# Display the results
print("\nSum of the 10 numbers:", total_sum)
print("Average of the 10 numbers:", average)
