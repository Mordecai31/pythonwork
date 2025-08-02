import streamlit as st
import datetime

st.title("Age Calculator")

# Date of Birth input
dob = st.date_input("Enter your Date of Birth:", max_value=datetime.date.today())

# Optional: Select target date (default: today)
target_date = st.date_input("Calculate age as of:", value=datetime.date.today())

# Validation
if dob > target_date:
    st.error("Date of birth cannot be in the future relative to the target date.")
else:
    # Calculate age difference
    delta = target_date - dob
    age_days = delta.days
    age_weeks = age_days // 7
    age_hours = age_days * 24

    # Age in years
    age_years = target_date.year - dob.year
    if (target_date.month, target_date.day) < (dob.month, dob.day):
        age_years -= 1

    # Age in months
    age_months = (target_date.year - dob.year) * 12 + (target_date.month - dob.month)
    if target_date.day < dob.day:
        age_months -= 1

    # Day of the week
    day_of_week = dob.strftime("%A")

    # Display results
    st.success(f"You were born on a {day_of_week}.")

    st.info(f"""
            As of {target_date}:
    - **Years**: {age_years}
    - **Months**: {age_months}
    - **Days**: {age_days}
    - **Weeks**: {age_weeks}
    - **Hours**: {age_hours}
    """)
