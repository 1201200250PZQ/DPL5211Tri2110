# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

def rectangle():
    area = width * length
    return area

def triangle():
    area = (1/2) * width * length
    return area

times =0
while(times<2):

    width = int(input("Enter width  : "))
    length = int(input("Enter length  : "))

    print("\nRectangle area : {:.2f}".format(rectangle()))
    print("Triangle area  : {:.2f}\n\n".format(triangle()))

    times = times + 1
