#  Student ID : 1201200250 #
#  Student Name : PAN ZHI QI #

hourly_rate = 6.50

# Get input of how many hours worked for a week
# calculate staff salary for one week
# if staff work more than 40 hours, overtime pay is 10.50 per hour for the additional hours.
# Staff can not work 60 hours per week, so only additional 20 hours is calculated for overtime pay.
# Display the salary

hour = int(input("How many hour you worked for a week : "))

ov_rate = 10.50

if (hour >= 60):
    extraovtime_p = (hour - 60) * hourly_rate
    print("Too much work")
    salary = (20 * ov_rate) + (40 * hourly_rate) + extraovtime_p

elif (hour >= 40 and hour <= 59):
    ov_pay = (hour - 40) * ov_rate
    total_p = 40 * hourly_rate
    salary = total_p + ov_pay


elif (hour < 40):
    salary = hour * hourly_rate

print("Your salary is RM {:.2f}".format(salary))