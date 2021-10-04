#  Student ID : 1201200250 #
#  Student Name : PAN ZHI QI #

# Get input for marks
# show grade based on the marks
# A 80 and above, B--> 70 and above, C is 50 and above, below 50 is fail
# invalis marks is more` than 100 or below 0
# using elif meaning else if 

marks = float(input("Enter your marks : "))

if (marks>=0 and marks<=100):
    if marks>=80:
        print("Your grade is : A")
    elif marks>=70:
        print("Your grade is : B")
    elif marks>=50:
        print("Your grade is : C")
    else:
        print("Your grade is : Fail")
else:
    print("Invalid marks!")