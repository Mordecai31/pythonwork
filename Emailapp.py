import streamlit as st
import re

# Title of the app
st.title("Email Slicer Tool")

# Description
st.write("Enter your email address below to extract the **username** and **domain**.")

# Get user input
email = st.text_input("Enter your email address:")

# Define the email slicer function
def email_slicer(email):
    # Use regex to validate a basic email structure
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$"
    if re.match(pattern, email):
        # Split email into username and domain
        username, domain = email.split('@')
        return username, domain
    else:
        return None, None

# If email is entered, process it
if email:
    username, domain = email_slicer(email)

    if username and domain:
        st.success("Email successfully sliced!")
        st.write(f"**Username**: `{username}`")
        st.write(f"**Domain**: `{domain}`")

        # Optional domain categorization
        if "gmail.com" in domain or "yahoo.com" in domain or "hotmail.com" in domain:
            st.info("This looks like a **personal email**.")
        else:
            st.info("This might be a **corporate or custom domain** email.")
    else:
        st.error("Invalid email format. Please try again.")
