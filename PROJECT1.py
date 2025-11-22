
def get_numerical_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def expense_manager():
    transactions = []
    current_balance = 0.0

    print("Welcome to the Monthly Expense and Income Manager!\n")

    while True:
        print("Menu:")
        print("1. Record Income")
        print("2. Record Expense")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            print("\n--- Record Income ---")
            description = input("Enter income description (e.g., Salary): ")
            amount = get_numerical_input("Enter income amount: $")
            transactions.append(('income', description, amount))
            current_balance += amount
            print("Income recorded successfully!\n")

        elif choice == '2':
            print("\n--- Record Expense ---")
            description = input("Enter expense description (e.g., Groceries): ")
            amount = get_numerical_input("Enter expense amount: $")

            transactions.append(('expense', description, amount))
            current_balance -= amount
            print("Expense recorded successfully!\n")

        elif choice == '3':
            print("\n" + "="*40)
            print("       TRANSACTION SUMMARY")
            print("="*40)

            if not transactions:
                print("No transactions recorded yet.")
            else:
                
                for trans in transactions:
                    trans_type, desc, amt = trans
                    if trans_type == 'income':
                        print(f"Income   : {desc.ljust(20)} | +${amt:.2f}")
                    else:
                        print(f"Expense  : {desc.ljust(20)} | -${amt:.2f}")

                total_income = 0.0
                total_expenses = 0.0
                for trans in transactions:
                    if trans[0] == 'income':
                        total_income += trans[2]
                    else:
                        total_expenses += trans[2]

                print("\n--- Monthly Totals ---")
                print(f"Total Income   : ${total_income:.2f}")
                print(f"Total Expenses : ${total_expenses:.2f}")
                print(f"Current Balance: ${current_balance:.2f}")
                
                if current_balance >= 0:
                    print("You're in the green! Keep it up! :)")
                else:
                    print("Warning: You're in the red! Watch your spending.")

            print("="*40 + "\n")

        elif choice == '4':
            print("Thank you for using Expense Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    expense_manager()