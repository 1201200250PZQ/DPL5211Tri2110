# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

# Given an array of 3,6,9,12,23 create another array containing the squared number of each number
# from the first array and display the second array

array = [3,6,9,12,23]
square = [] #empty array

for squareindex in range(0, 5):
    square.append(array[squareindex]*array[squareindex])
    print(square[squareindex])


#studnames.reverse  ...reverse list
#studnames.append  ...to add a new value
#studnames.remove  ...to remove the value