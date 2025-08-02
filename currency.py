import streamlit as st
import requests

# Predefined fallback rates (for offline use)
offline_rates = {
    "USD": {"EUR": 0.92, "NGN": 1500, "GBP": 0.78},
    "EUR": {"USD": 1.09, "NGN": 1635, "GBP": 0.85},
    "NGN": {"USD": 0.00067, "EUR": 0.00061, "GBP": 0.00052},
    "GBP": {"USD": 1.28, "NGN": 1800, "EUR": 1.18}
}

# Function to fetch real-time exchange rates
def get_exchange_rates(base_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["rates"]
        else:
            return None
    except:
        return None

# Streamlit UI
st.title("Currency Converter")

base_currency = st.selectbox("Base Currency", ["USD", "EUR", "NGN", "GBP"])
target_currency = st.selectbox("Target Currency", ["USD", "EUR", "NGN", "GBP"])
amount = st.number_input("Enter Amount", min_value=0.0, step=1.0)

if st.button("Convert"):
    if base_currency == target_currency:
        st.info("Same currency selected. Conversion not needed.")
    else:
        # Try online first
        rates = get_exchange_rates(base_currency)
        
        if rates and target_currency in rates:
            rate = rates[target_currency]
            converted = round(amount * rate, 2)
            st.success(f"{amount} {base_currency} = {converted} {target_currency} (Online Rate)")
        elif base_currency in offline_rates and target_currency in offline_rates[base_currency]:
            rate = offline_rates[base_currency][target_currency]
            converted = round(amount * rate, 2)
            st.warning(f"{amount} {base_currency} = {converted} {target_currency} (Offline Rate)")
        else:
            st.error("Conversion not possible. Check currency codes or internet.")
