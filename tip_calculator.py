print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))

bill_plus_tip = tip/100 * bill + bill

bill_per_person = format(bill_plus_tip / people,".2f")
print(f"Each person should pay: ${bill_per_person}")
