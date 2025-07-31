print("Welcome to Expense Tracker")

expense_name = input("Enter expense name: ")
expense_amount =float(input("Enter amount (Ksh): "))

with open("expenses.txt", "a") as file:
    file.write(f"{expense_name}: Ksh {expense_amount}\n")

    print("Expense saved!")