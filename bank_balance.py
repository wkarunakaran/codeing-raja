import json

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount, transaction_type):
        self.transactions.append({"category": category, "amount": amount, "type": transaction_type})

    def calculate_budget(self):
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        total_expenses = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def expense_analysis(self):
        expense_by_category = {}
        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]
                amount = transaction["amount"]
                if category in expense_by_category:
                    expense_by_category[category] += amount
                else:
                    expense_by_category[category] = amount
        return expense_by_category

    def save_transactions(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file)

    def load_transactions(self, filename):
        with open(filename, 'r') as file:
            self.transactions = json.load(file)

def main():
    tracker = BudgetTracker()

    while True:
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Save Transactions")
        print("6. Load Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_transaction(category, amount, "expense")
        elif choice == "2":
            category = input("Enter income source: ")
            amount = float(input("Enter income amount: "))
            tracker.add_transaction(category, amount, "income")
        elif choice == "3":
            print("Remaining Budget:", tracker.calculate_budget())
        elif choice == "4":
            print("Expense Analysis:", tracker.expense_analysis())
        elif choice == "5":
            filename = input("Enter filename to save transactions: ")
            tracker.save_transactions(filename)
            print("Transactions saved successfully.")
        elif choice == "6":
            filename = input("Enter filename to load transactions: ")
            tracker.load_transactions(filename)
            print("Transactions loaded successfully.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
