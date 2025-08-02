import streamlit as st
import time

# Title of the app
st.title("Countdown Timer")

# Sidebar input for minutes and seconds
minutes = st.sidebar.number_input("Minutes", min_value=0, value=0)
seconds = st.sidebar.number_input("Seconds", min_value=0, max_value=59, value=10)

# Total time in seconds
total_seconds = int(minutes * 60 + seconds)

# Button to start the timer
if st.button("Start Timer"):
    placeholder = st.empty()
    progress_bar = st.progress(0)

    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        placeholder.markdown(f"#Time Left: {time_display}")
        progress = (total_seconds - remaining) / total_seconds
        progress_bar.progress(progress)
        time.sleep(1)

    placeholder.markdown("#Time's up!")
    st.balloons()