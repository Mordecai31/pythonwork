import streamlit as st

# Title of the app
st.title("Simple Chatbot")

# Instructions
st.write("Type a message below and get a response from the bot. Type `'bye'` to exit.")

# Dictionary of predefined responses
responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm doing great!",
    "what is python": "Python is a programming language used for various applications.",
    "where are you learning data science": "Sail Innovation Lab",
    "what programming language are you learning?": "Python",
    "bye": "Goodbye! Have a great day!"
}

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input box for user message
user_input = st.text_input("You:", "")

# If user submits a message
if user_input:
    user_input_lower = user_input.lower().strip()

    # Get bot response
    if user_input_lower in responses:
        bot_response = responses[user_input_lower]
    else:
        bot_response = "I'm sorry, I don't understand that."

    # Save message to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

    # Clear input box after submission
    st.experimental_rerun()

# Display the full chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
