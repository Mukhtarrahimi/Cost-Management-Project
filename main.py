import csv
import os
from datetime import date

FILE_NAME = "data.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "type", "amount", "note"])


def add_transaction(tx_type, amount, note):
    today = date.today().isoformat()
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([today, tx_type, amount, note])
    print("Transaction saved.")


def show_transactions():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("\ntransactions list:")
        for row in reader:
            print(f"{row['date']} | {row['type']} | {row['amount']} | {row['note']}")


def summary():
    income, expense = 0, 0
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["type"] == "income":
                income += float(row["amount"])
            elif row["type"] == "expense":
                expense += float(row["amount"])
    balance = income - expense
    print("\n Summary:")
    print(f"Income: {income}")
    print(f"Expense: {expense}")
    print(f"Balance: {balance}")


def menu():
    while True:
        print("\n=== Expense Management System ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Transactions")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            amount = input("Income amount: ")
            note = input("Description: ")
            add_transaction("income", amount, note)
        elif choice == "2":
            amount = input("Expense amount: ")
            note = input("Description: ")
            add_transaction("expense", amount, note)
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
