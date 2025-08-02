import streamlit as st
import datetime
import json
import os

# Path to store birthday data
FILE = "birthdays.json"

# Load birthdays from a file
def load_birthdays():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save birthdays to a file
def save_birthdays(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Day suffix helper
def day_suffix(day):
    if 11 <= day <= 13:
        return "th"
    last = day % 10
    return {1: "st", 2: "nd", 3: "rd"}.get(last, "th")

# Load existing data
birthdays = load_birthdays()

# Streamlit UI
st.title("Birthday Reminder App")
today = datetime.date.today()
st.info(f"Today: {today.strftime('%A, %B %d, %Y')}")

# Add new birthday
st.header("Add a New Birthday")
with st.form("add_birthday"):
    name = st.text_input("Enter name")
    dob = st.date_input("Enter birthday")
    submitted = st.form_submit_button("Save")
    if submitted:
        if name:
            birthdays[name] = dob.strftime("%Y-%m-%d")
            save_birthdays(birthdays)
            st.success(f"Birthday for {name} saved: {dob.strftime('%B %d, %Y')}")
        else:
            st.warning("Name cannot be empty.")

# Show reminders
st.header("Today's and Upcoming Birthdays")
today_found = False
for name, date_str in birthdays.items():
    try:
        bday = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if bday.month == today.month and bday.day == today.day:
            st.success(f"Reminder: {name}'s birthday is today!")
            today_found = True
        elif bday.month == today.month:
            suffix = day_suffix(bday.day)
            formatted = f"{bday.strftime('%B')} {bday.day}{suffix}"
            st.info(f"Upcoming: {name}'s birthday is on {formatted}")
    except Exception as e:
        st.error(f"Error parsing birthday for {name}: {e}")

if not today_found:
    st.write("No birthdays today.")

# View all birthdays
if st.checkbox("Show All Saved Birthdays"):
    st.table({name: date for name, date in birthdays.items()})
