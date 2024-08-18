# Personal Finance Tracker

This is a simple Python-based personal finance tracker that allows users to manage and analyze their financial transactions. It supports adding new transactions, viewing transactions within a specified date range, and generating a summary along with a plot of income and expenses over time.

Features:

- **Add Transactions**: Record your income or expenses with details like date, amount, category, and description.
- **View Transactions**: Filter and view your transactions within a specific date range.
- **Summary Generation**: Get a summary of your total income, total expenses, and net savings for the selected date range.
- **Visualization**: Option to generate a plot that visually represents your income and expenses over time.

Getting Started:

Prerequisites:

Ensure you have Python installed on your system. You will also need the following Python packages:

- `pandas`
- `matplotlib`

You can install the necessary packages using pip:

```bash
pip install pandas matplotlib
```

### Files

- **my_finance_data.csv**: The CSV file where transaction data will be stored. It will be created automatically if it doesn't exist.
- **finance_tracker.py**: The main script containing all the code to run the personal finance tracker.

### Running the Application

1. Clone this repository or download the `finance_tracker.py` file.

2. Ensure you are in the directory containing the `finance_tracker.py` script.

3. Run the script using Python:

   ```bash
   python finance_tracker.py
   ```

4. Follow the on-screen prompts to add transactions, view transaction summaries, or generate visual plots.

Usage:

Adding a Transaction

1. Select the option to add a new transaction.
2. Enter the transaction date (format: `dd-mm-yyyy`), or press Enter to use today's date.
3. Enter the transaction amount.
4. Specify whether the transaction is an Income (`I`) or an Expense (`E`).
5. Optionally, provide a description for the transaction.
6. The transaction will be saved to the `my_finance_data.csv` file.

Transactions and Summary

1. Select the option to view transactions.
2. Enter the start and end dates (format: `dd-mm-yyyy`) for the range you wish to view.
3. The application will display the filtered transactions and provide a summary of total income, total expenses, and net savings.
4. If you wish, you can generate a plot showing your income and expenses over time.

Functions Overview

- **`initialize_csv()`**: Initializes the CSV file if it does not already exist.
- **`add_transaction(date, amount, category, description)`**: Adds a new transaction to the CSV file.
- **`get_transactions(start_date, end_date)`**: Retrieves transactions within the specified date range and generates a summary.
- **`plot_transactions(df)`**: Plots income and expenses over time using matplotlib.
- **User Input Functions**: Functions like `get_date()`, `get_amount()`, `get_category()`, and `get_description()` handle user input for various transaction details.

Acknowledgments:

- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

This tool was created to help manage personal finances easily using a Python script.
