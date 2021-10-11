# Student ID: 1201200250 #
# Student Name: PAN ZHI QI #

def get_bonus(unit, salary):
    if(unit>1000):
        bonus = salary * 0.2

    elif(unit>500):
        bonus = salary * 0.1
    
    else:
        bonus = 0
    
    return bonus

def get_nett_salary(salary,bonus):
    nett_salary = bonus + salary
    return nett_salary

def display(staff_id, salary, unit, bonus, nett_salary):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("               SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                :  {}".format(staff_id))
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              :  {}" .format(unit))
    print("Bonus                   :  RM {:.2f}" .format(bonus))
    print("Nett Salary             :  RM {:.2f}" .format(nett_salary))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
staff_id = int(input("Enter staff id          : "))
salary = float(input("Enter staff salary      : RM "))
unit = int(input("Enter total units sold  : "))

bonus = get_bonus(unit, salary)

nett_salary = get_nett_salary(salary,bonus)

display(staff_id, salary, unit, bonus, nett_salary)