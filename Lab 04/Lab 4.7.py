# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

# Display the name in reverse order studnames[0] = "Law Qian Er", studnames[2] = "Khoo Chong Qin"

studnames = ["Law Qian Er", "Wong Bing Jie", "Khoo Chong Qin"]
studnames.append("Suhaimi")
for name in reversed(studnames):
    print(name)


for studindex in range(3, -1, -1):
    print(studnames[studindex])


#studnames.reverse  ...reverse list
#studnames.append  ...to add a new value
#studnames.remove  ...to remove the value