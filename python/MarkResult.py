Mask=int(input("enter your mark: "))
if(Mask<35):
    print("Poor Students")
elif(Mask>90 and Mask<100):
    print("Your Grade is A+, Very excellent Mark")
elif(Mask>80 and Mask<89):
    print("Your Grade is A, Excellent Mark")
elif(Mask>70 and Mask<79):
    print("Your Grade is B+, Very Good Mark")
elif(Mask>60 and Mask<69):
    print("Your Grade is B, Good Mark")
elif(Mask>50 and Mask<59):
    print("Your Grade is C+, Average Mark")
elif(Mask>35 and Mask<49):
    print("Your Grade is C, Below Average Mark")
else:
    print("invalid Input")