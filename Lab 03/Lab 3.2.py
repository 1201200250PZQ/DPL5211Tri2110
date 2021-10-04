#  Student ID : 1201200250 #
#  Student Name : PAN ZHI QI #

cur_balance = 30.12

# get_input from user to withdraw money how much money
# if balance is less RM 10, alert the user that there is no sufficient fund.
# and display the current balance.
# use else: to of the current balance is sufficient and 
# display the new current balance.

withdraw = float(input("Enter the withdraw amount : RM "))


new_balance = cur_balance - withdraw


if new_balance < 10 :

    print("Your balance is not sufficient")

else :

    print("Your new balance is : RM {:.2f}" .format(new_balance))