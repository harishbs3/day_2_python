print("\tWelcome to the tip calculator!")
bill_amount= float(input("Enter the bill amount:\n"))
tip = int(input("Enter tip in %:\n"))
total_bill = bill_amount+(bill_amount*(tip*0.01))
no_of_persons = int(input("No of persons you want to split the Bill with: \n"))
amount_to_pay = total_bill/no_of_persons
print(f"Each person has to pay ${amount_to_pay}")