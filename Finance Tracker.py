import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "my_finance_data.csv"
DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}



def initialize_csv():
    try:
        pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])


def add_transaction(date, amount, category, description):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Transaction added successfully.")



def get_transactions(start_date, end_date):
    df = pd.read_csv(CSV_FILE)
    df["Date"] = pd.to_datetime(df["Date"], format=DATE_FORMAT)
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)

    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    
    if filtered_df.empty:
        print("No transactions found in the given date range.")
    else:
        print(f"Transactions from {start_date.strftime(DATE_FORMAT)} to {end_date.strftime(DATE_FORMAT)}")
        print(filtered_df.to_string(index=False, date_format=DATE_FORMAT))
        
        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
        net_savings = total_income - total_expense

        print(f"\nSummary:\nTotal Income: ${total_income:.2f}\nTotal Expense: ${total_expense:.2f}\nNet Savings: ${net_savings:.2f}")

    return filtered_df



# plot transactions
def plot_transactions(df):
    df.set_index("Date", inplace=True)
    income_df = df[df["Category"] == "Income"].resample("D").sum().fillna(0)
    expense_df = df[df["Category"] == "Expense"].resample("D").sum().fillna(0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="green")
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="red")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income vs Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



# user inputs
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)
    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return get_date(prompt, allow_default)




def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be a positive value.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")



# Main function 
def main():
    initialize_csv()
    
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            date = get_date("Enter the transaction date (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
            amount = get_amount()
            category = get_category()
            description = get_description()
            add_transaction(date, amount, category, description)
        
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = get_transactions(start_date, end_date)
            if not df.empty:
                if input("Do you want to see a plot? (y/n): ").lower() == 'y':
                    plot_transactions(df)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
