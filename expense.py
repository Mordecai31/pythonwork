import streamlit as st
import csv
import pandas as pd
from datetime import datetime

FILENAME = "expenses.csv"

# Function to add an expense to CSV
def add_expense(date, category, amount, description):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

# Load expenses from CSV into a DataFrame
def load_expenses():
    try:
        df = pd.read_csv(FILENAME, names=["Date", "Category", "Amount", "Description"])
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Streamlit UI
st.title("Basic Expense Tracker")

# Add new expense
with st.form("Add Expense"):
    st.subheader("Add New Expense")
    date = st.date_input("Date", datetime.today())
    category = st.selectbox("Category", ["Food", "Transport", "Groceries", "Bills", "Others"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        add_expense(date.strftime("%Y-%m-%d"), category, amount, description)
        st.success("Expense added successfully!")

# Load and display existing expenses
st.subheader("View Expenses")

df = load_expenses()

# Filter by date range
with st.expander("Filter by Date Range"):
    start_date = st.date_input("Start Date", df["Date"].min() if not df.empty else datetime.today())
    end_date = st.date_input("End Date", df["Date"].max() if not df.empty else datetime.today())
    df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

if not df.empty:
    st.dataframe(df)

    # Summary by category
    st.subheader("Summary by Category")
    summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    st.bar_chart(summary)
    st.write(summary)
else:
    st.info("No expenses to display yet.")