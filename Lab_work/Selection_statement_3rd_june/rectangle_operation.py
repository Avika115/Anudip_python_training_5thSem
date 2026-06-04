#Program to calculate area and perimeter of a rectangle
#input the values
length = int(input("Enter length: "))
width = int(input("Enter width: "))
#------------------------------------
#validate the input
if (length > 0 and width > 0):
    area = length * width
    perimeter = 2 * (length + width)
#displaying the area and perimeter
    print("Area =", area)
    print("Perimeter =", perimeter)
#--------------------
else:
    exit("the input is invalid")