import streamlit as st
import random

st.title("Number Guessing Game")

# Initialize session state
if 'number' not in st.session_state:
    st.session_state.number = random.randrange(5, 100, 5)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10
    st.session_state.best_score = None

st.write("Guess the number (multiples of 5 between 5 and 100).")

# Input field
guess = st.number_input("Enter your guess:", min_value=5, max_value=100, step=5, format="%d")

# Guess button
if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low!")
    elif guess > st.session_state.number:
        st.warning("Too high!")
    else:
        st.success(f"Correct! You guessed it in {st.session_state.attempts} attempts.")
        if st.session_state.best_score is None or st.session_state.attempts < st.session_state.best_score:
            st.session_state.best_score = st.session_state.attempts
            st.balloons()
            st.info("New best score!")
        st.session_state.number = random.randrange(5, 100, 5)
        st.session_state.attempts = 0

    if st.session_state.attempts >= st.session_state.max_attempts:
        st.error(f"Game over! The number was {st.session_state.number}. Starting a new game...")
        st.session_state.number = random.randrange(5, 100, 5)
        st.session_state.attempts = 0

# Display scores
st.write(f"Attempts: {st.session_state.attempts} / {st.session_state.max_attempts}")
if st.session_state.best_score:
    st.write(f"Best Score: {st.session_state.best_score}")