def add_expense():
        name = input("Enter expense name: ")
            amount = input("Enter amount (Ksh): ")
                with open("expenses.txt", "a") as file:
                        file.write(f"{name} Ksh {amount}\n")
                            print("✅ Expense saved!\n")

                            def view_expenses():
                                try:
                                        with open("expenses.txt", "r") as file:
                                                    lines = file.readlines()
                                                                if lines:
                                                                                print("\n📋 Saved Expenses:")
                                                                                                for line in lines:
                                                                                                                    print("•", line.strip())
                                                                                                                                else:
                                                                                                                                                print("📭 No expenses recorded.")
                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                            print("🚫 No expenses file found.")

                                                                                                                                                            def search_expense():
                                                                                                                                                                keyword = input("🔍 Enter keyword to search: ").lower()
                                                                                                                                                                    try:
                                                                                                                                                                            with open("expenses.txt", "r") as file:
                                                                                                                                                                                        matches = [line.strip() for line in file if keyword in line.lower()]
                                                                                                                                                                                                    if matches:
                                                                                                                                                                                                                    print("\n🔎 Matching Expenses:")
                                                                                                                                                                                                                                    for match in matches:
                                                                                                                                                                                                                                                        print("•", match)
                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                    print("❌ No matching expenses found.")
                                                                                                                                                                                                                                                                                        except FileNotFoundError:
                                                                                                                                                                                                                                                                                                print("🚫 No expenses file found.")

                                                                                                                                                                                                                                                                                                # Menu
                                                                                                                                                                                                                                                                                                while True:
                                                                                                                                                                                                                                                                                                    print("\n=== Expense Tracker Menu ===")
                                                                                                                                                                                                                                                                                                        print("1. Add Expense")
                                                                                                                                                                                                                                                                                                            print("2. View Expenses")
                                                                                                                                                                                                                                                                                                                print("3. Search Expense")
                                                                                                                                                                                                                                                                                                                    print("4. Exit")
                                                                                                                                                                                                                                                                                                                        choice = input("Choose an option (1-4): ")

                                                                                                                                                                                                                                                                                                                            if choice == "1":
                                                                                                                                                                                                                                                                                                                                    add_expense()
                                                                                                                                                                                                                                                                                                                                        elif choice == "2":
                                                                                                                                                                                                                                                                                                                                                view_expenses()
                                                                                                                                                                                                                                                                                                                                                    elif choice == "3":
                                                                                                                                                                                                                                                                                                                                                            search_expense()
                                                                                                                                                                                                                                                                                                                                                                elif choice == "4":
                                                                                                                                                                                                                                                                                                                                                                        print("👋 Goodbye!")
                                                                                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                            print("❗ Invalid choice. Please select 1-4.")

print("\n--- Expense Summary ---")

try:
    with open("expenses.txt", "r") as file:
            total = 0
                    count = 0
                            for line in file:
                                        line = line.strip()
                                                    if "Ksh" in line:
                                                                    try:
                                                                                        parts = line.split("Ksh")
                                                                                                            amount = float(parts[1].strip().replace(",", ""))
                                                                                                                                total += amount
                                                                                                                                                    count += 1
                                                                                                                                                                    except (IndexError, ValueError):
                                                                                                                                                                                        continue  # skip lines with issues
                                                                                                                                                                                                print("Total Expenses: Ksh", total)
                                                                                                                                                                                                        print("Number of Expenses:", count)
                                                                                                                                                                                                        except FileNotFoundError:
                                                                                                                                                                                                            print("No expenses found.")