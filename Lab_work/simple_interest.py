#Program to calculate simple interest
#input the values
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))
#------------------------------------------------

#validate input
if(principal<=0):
    exit("Principal should be greater than 0")
#--------------------------
elif(rate<0):
    exit("rate cannot be negative")
#--------------------------
elif(time<=0):
    exit("time must be greater than 0")
#--------------------------
#displaying the interest
else:
    si=(principal*rate*time)/100
    print("simple interest=",si)