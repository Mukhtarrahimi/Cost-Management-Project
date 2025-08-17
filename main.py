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


def search_transactions(keyword):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        found = False
        print(f"\n Search results for: {keyword}")
        for row in reader:
            if (
                keyword in row["date"]
                or keyword in row["type"]
                or keyword in row["amount"]
                or keyword in row["note"]
            ):
                print(
                    f"{row['date']} | {row['type']} | {row['amount']} | {row['note']}"
                )
                found = True
        if not found:
            print("nothing found.")


def delete_transaction():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    if not reader:
        print("no transactions found.")
        return

    print("\n List of transactions to delete:")
    for i, row in enumerate(reader, start=1):
        print(f"{i}. {row['date']} | {row['type']} | {row['amount']} | {row['note']}")

    try:
        choice = int(input("Enter the transaction number to delete: "))
        if 1 <= choice <= len(reader):
            removed = reader.pop(choice - 1)
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["date", "type", "amount", "note"]
                )
                writer.writeheader()
                writer.writerows(reader)
            print(
                f"Transaction deleted: {removed['date']} | {removed['type']} | {removed['amount']} | {removed['note']}"
            )
        else:
            print("Invalid number.")
    except ValueError:
        print("Input must be a number.")


def edit_transaction():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    if not reader:
        print("no transactions found.")
        return

    print("\n List of transactions to edit:")
    for i, row in enumerate(reader, start=1):
        print(f"{i}. {row['date']} | {row['type']} | {row['amount']} | {row['note']}")

    try:
        choice = int(input("Enter the transaction number to edit: "))
        if 1 <= choice <= len(reader):
            tx = reader[choice - 1]
            print("\n Enter new values (leave blank to keep current):")
            new_type = input(f"Type ({tx['type']}): ") or tx["type"]
            new_amount = input(f"Amount ({tx['amount']}): ") or tx["amount"]
            new_note = input(f"Description ({tx['note']}): ") or tx["note"]

            # update
            reader[choice - 1] = {
                "date": tx["date"],
                "type": new_type,
                "amount": new_amount,
                "note": new_note,
            }

            # save again
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["date", "type", "amount", "note"]
                )
                writer.writeheader()
                writer.writerows(reader)

            print(" Transaction edited successfully.")
        else:
            print(" Invalid number.")
    except ValueError:
        print(" Input must be a number.")


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
