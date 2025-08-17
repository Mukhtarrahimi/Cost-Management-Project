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
