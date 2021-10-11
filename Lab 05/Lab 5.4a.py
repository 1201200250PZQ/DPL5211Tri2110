# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

def rectangle():
    area = width * length
    return area

def triangle():
    area = (1/2) * width * length
    return area

width = int(input("Enter width  : "))
length = int(input("Enter length  : "))

print("\nRectangle area : {:.2f}".format(rectangle()))
print("Triangle area  : {:.2f}".format(triangle()))
