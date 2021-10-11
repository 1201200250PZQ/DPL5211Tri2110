# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

def get_cm():
    cm = float(input("Enter centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters equals to {:.2f} meters ".format(cm, m))

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_meter():
    m = float(input("Enter meter : "))
    cm = meter_to_cm(m)
    print("{:.2f} meters equals to {:.2f} centimeters ".format(m, cm))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

print("======================================")
print("                 MENU                 ")
print("======================================")
print(" 1.    Convert centimeter to meter")
print(" 2.    Convert meter to centimeter")

choice = int(input("Enter your choice [1 or 2] : "))

if (choice == 1):
    get_cm()

elif(choice == 2):
    get_meter()

else:
    print("Invalid choice")

