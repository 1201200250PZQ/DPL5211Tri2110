# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

#get the input for a number from 1 until 12 using the for loop display the multiplication tables

num = int(input("Please input a number from 1 until 12: "))

for i in range (1,13):
    print(i, " x ", num, " = ", num*i)