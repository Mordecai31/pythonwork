import streamlit as st

#conversion functions
def meters_to_kilometers(meters):
    return round(meters/1000,3)
def kilometers_to_miles(km):
    return round(km*0.621371,3)
def celsius_to_fahrenheit(c):
    return round((c * 9 / 5) + 32, 3)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5 / 9, 3)

def grams_to_kilograms(grams):
    return round(grams / 1000, 3)

st.title("Unit Converter")

conversion_type=st.selectbox(
    "Select a conversion:",
    [
        "meters_to_kilometers",
        "Kilometers to Miles",
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Grams to kilograms"
    ]
)
value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
if st.button("Convert"):
    if conversion_type == "Meters to Kilometers":
        result = meters_to_kilometers(value)
        st.success(f"{value} meters is {result} kilometers")
    elif conversion_type == "Kilometers to Miles":
        result = kilometers_to_miles(value)
        st.success(f"{value} kilometers is {result} miles")
    elif conversion_type == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(value)
        st.success(f"{value} °C is {result} °F")
    elif conversion_type == "Fahrenheit to Celsius":
        result = fahrenheit_to_celsius(value)
        st.success(f"{value} °F is {result} °C")
    elif conversion_type == "Grams to Kilograms":
        result = grams_to_kilograms(value)
        st.success(f"{value} grams is {result} kilograms")
        