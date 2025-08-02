import streamlit as st
import re

# Function using two-pointer approach for long strings
def is_palindrome(word):
    word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

# Streamlit interface
st.set_page_config(page_title="Palindrome Checker")
st.title("Palindrome Checker")

# Input from user
text_input = st.text_area("Enter word(s), phrase(s), or number(s):", height=150,
                          placeholder="One per line...")

# When button is clicked
if st.button("Check"):
    if not text_input.strip():
        st.warning("Please enter at least one word or phrase.")
    else:
        st.subheader("Results")
        lines = text_input.strip().splitlines()

        for line in lines:
            cleaned = line.strip()
            if cleaned:
                result = "Palindrome" if is_palindrome(cleaned) else "Not a Palindrome"
                st.write(f"**{cleaned}**{result}")