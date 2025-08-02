import streamlit as st
import random

st.title("Rock paper game")

#option for advanced mode
advanced_mode=st.checkbox("Enabled Advanced mode(lizard,spock)")

# Define choices
basic_choices = ["rock", "paper", "scissors"]
advanced_choices = basic_choices + ["lizard", "spock"]
choices = advanced_choices if advanced_mode else basic_choices

#rules
rules={"rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}
# Initialize scores in session
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# User input
user_choice = st.selectbox("Choose your move:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"Computer chose: **{computer_choice.capitalize()}**")
    
    if user_choice == computer_choice:
        st.info("It's a draw!")
    elif computer_choice in rules[user_choice]:
        st.success("You win!")
        st.session_state.user_score += 1
    else:
        st.error("Computer wins!")
        st.session_state.computer_score += 1

    st.markdown("---")
    st.subheader("Scoreboard")
    st.write(f"You: {st.session_state.user_score} | computer: {st.session_state.computer_score}")

# Reset button
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Game reset!")