from tkinter import *
import sqlite3

# function to add expense
def add_expense():
    name = expense_name.get()
    amount = amount_entry.get()
    category = category_entry.get()

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (name, amount, category) VALUES (?, ?, ?)",
        (name, amount, category)
    )

    conn.commit()
    conn.close()

    print("Expense Added Successfully!")

    # clear boxes
    expense_name.delete(0, END)
    amount_entry.delete(0, END)
    category_entry.delete(0, END)


# function to view expenses
def view_expenses():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    print("\n----- Expenses -----")

    for row in rows:
        print(row)


# window
root = Tk()
root.title("Smart Expense Tracker")
root.geometry("400x400")

# heading
title_label = Label(root, text="Expense Tracker",
font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# expense name
Label(root, text="Expense Name").pack()
expense_name = Entry(root, width=30)
expense_name.pack()

# amount
Label(root, text="Amount").pack()
amount_entry = Entry(root, width=30)
amount_entry.pack()

# category
Label(root, text="Category").pack()
category_entry = Entry(root, width=30)
category_entry.pack()

# add button
Button(root, text="Add Expense",
command=add_expense).pack(pady=10)

# view button
Button(root, text="View Expenses",
command=view_expenses).pack()

root.mainloop()