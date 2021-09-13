# Student ID : 1201200250
# Student Name : PAN ZHI QI

print("Invoice for Fruits Purchase")
print("-----------------------------------")

BANANAS = 1.5
GRAPES = 5.6

qtybananas = int(input("Enter the amount (comb) of bananas bought: "))
qtygrapes = int(input("Enter the amount (kg) of grapes bought: ")) 

totalbananas = (BANANAS * qtybananas)
totalgrapes = (GRAPES * qtygrapes)
total = (BANANAS * qtybananas) + (GRAPES * qtygrapes)

print("\nItem \t\t Qty \t Price \t\t Total")
print("Bananas (combs)   {} \t RM{:.2f} \t RM{:.2f}".format(qtybananas,BANANAS,totalbananas))
print("Grapes (kg) \t  {} \t RM{:.2f} \t RM{:.2f}".format(qtygrapes,GRAPES,totalgrapes))

print("\nTotal: RM{:.2f}".format(total))