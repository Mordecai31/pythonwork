import streamlit as st
import math

# Define calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else ("Math Error")
def exponent(a, b): return a ** b
def square_root(a): return math.sqrt(a)

# Streamlit App
st.title("Simple Calculator App")

st.markdown("**Choose an operation below and input your numbers.**")

# Operation selection
operation = st.selectbox("Select Operation", (
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)",
    "Exponentiation (x^y)",
    "Square Root (√x)"
))

# Input fields based on operation
if operation == "Square Root (√x)":
    num1 = st.number_input("Enter a number", format="%.2f")
    if st.button("Calculate"):
        result = square_root(num1)
        st.success(f"Square root of {num1} is {result:.2f}")
else:
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    if st.button("Calculate"):
        if operation == "Addition (+)":
            result = add(num1, num2)
        elif operation == "Subtraction (-)":
            result = subtract(num1, num2)
        elif operation == "Multiplication (×)":
            result = multiply(num1, num2)
        elif operation == "Division (÷)":
            result = divide(num1, num2)
        elif operation == "Exponentiation (x^y)":
            result = exponent(num1, num2)
        else:
            result = "Invalid operation"

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"Result: {result:.2f}")

# Exit option - in Streamlit this typically means the user just closes the app
st.markdown("To exit, simply **close this tab or stop the Streamlit server.**")