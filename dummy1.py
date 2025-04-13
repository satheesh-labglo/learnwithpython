count=0

s1=float(input("1st Year, 1st Sem Mark "))
s2=float(input("1st Year, 2nd Sem Mark "))
s3=float(input("2nd Year, 1st Sem Mark "))
s4=float(input("2nd Year, 2nd Sem Mark "))
s5=float(input("3rd Year, 1st Sem Mark "))
s6=float(input("3rd Year, 2nd Sem Mark "))

total = s1+s2+s3+s4+s5+s6
percentage=total/6

Year=["1st Year","2nd year","3rd Year"]
Sem=["1st Sem", "2nd Sem"]


for i in Year:
    for j in Sem:
        #print(f'{i},{j} have result is')
        count=count+1
print("total Sem count is ",count)
print("Total Sem mark percentage : ", percentage)