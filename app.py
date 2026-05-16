import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Page title
st.set_page_config(page_title="Smart Expense Tracker", layout="wide")

st.title("💰 Personal Expense Manager")

st.caption("Built by Pradeepthi Samineni")

# Database connection
conn = sqlite3.connect("expense.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount REAL,
    category TEXT
)
""")
conn.commit()

# Sidebar
st.sidebar.header("Add Expense")

expense_name = st.sidebar.text_input("Expense Name")
amount = st.sidebar.number_input("Amount", min_value=0.0)
category = st.sidebar.selectbox(
    "Category",
    [
"Food",
"Transport",
"Shopping",
"Education",
"Entertainment",
"Bills and Recharges",
"Savings",
"Miscellaneous"
]
)

# Add button
if st.sidebar.button("Add Expense"):
    cursor.execute(
        "INSERT INTO expenses (name, amount, category) VALUES (?, ?, ?)",
        (expense_name, amount, category)
    )
    conn.commit()
    st.sidebar.success("Expense Added Successfully!")

# Show data
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=["ID", "Name", "Amount", "Category"])

# Expense table
st.subheader("Expense History")
st.dataframe(df)

# Total spending
if not df.empty:
    total = df["Amount"].sum()
    st.metric("Total Spending", f"₹{total}")

    # Pie chart
    category_sum = df.groupby("Category")["Amount"].sum().reset_index()

    fig = px.pie(
        category_sum,
        values="Amount",
        names="Category",
        title="Expense Distribution"
    )

    st.plotly_chart(fig)