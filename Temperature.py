import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# App title
st.title("Temperature Converter")

# Conversion options
options = {
    "Celsius to Fahrenheit": celsius_to_fahrenheit,
    "Fahrenheit to Celsius": fahrenheit_to_celsius,
    "Celsius to Kelvin": celsius_to_kelvin,
    "Kelvin to Celsius": kelvin_to_celsius,
    "Fahrenheit to Kelvin": fahrenheit_to_kelvin,
    "Kelvin to Fahrenheit": kelvin_to_fahrenheit
}

# Select conversion type
conversion_type = st.selectbox("Choose a conversion:", list(options.keys()))

# Input temperature
temp_input = st.text_input("Enter the temperature value:")

# Perform conversion
if temp_input:
    try:
        temp_value = float(temp_input)

        # Kelvin validation
        if "Kelvin" in conversion_type and "to Celsius" in conversion_type or "to Fahrenheit" in conversion_type:
            if temp_value < 0:
                st.error("Kelvin cannot be negative.")
            else:
                result = options[conversion_type](temp_value)
                st.success(f"**{conversion_type}:** {temp_value:.2f}{result:.2f}")
        else:
            result = options[conversion_type](temp_value)
            st.success(f"**{conversion_type}:** {temp_value:.2f} {result:.2f}")

    except ValueError:
        st.error("Please enter a valid number for temperature.")