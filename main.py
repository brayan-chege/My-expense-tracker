print("Welcome to Expense Tracker")

expense_name = input("Enter expense name: ")
expense_amount =float(input("Enter amount (Ksh): "))

with open("expenses.txt", "a") as file:
    file.write(f"{expense_name}: Ksh {expense_amount}\n")

    print("Expense saved!")

def view_expenses():
        try:
                with open("expenses.txt", "r") as file:
                            expenses = file.readlines()
                                        if not expenses:
                                                        print("No expenses found.")
                                                                    else:
                                                                                    print("Your saved expenses:")
                                                                                                    for line in expenses:
                                                                                                                        print(line.strip())
                                                                                                                            except FileNotFoundError:
                                                                                                                                    print("No expenses found. You haven't added any yet.")