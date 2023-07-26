import csv
import os

def initialize_data_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Date', 'Category', 'Description', 'Amount'])

def add_expense(filename, date, category, description, amount):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([date, category, description, amount])

def view_expense(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

def main():
    data_file = "expenses.csv"
    initialize_data_file(data_file)

    while True:
        print("\n ======Personal Finance Tracker======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date = input("Enter the date (DD/MM/YYYY): ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            add_expense(data_file, date, category, description, amount)
            print("Expense added successfully!")

        elif choice == '2':
            print("\n ==== Expense ====")
            view_expense(data_file)

        elif choice == '3':
            print("Exiting the Personal Finance Tracker. GoodBye!")
            break

        else:
            print("Invalid Choice. Please try again!")

if __name__ == "__main__":
    main()
