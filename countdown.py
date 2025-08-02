import streamlit as st
import time
import platform

# Optional sound alert for Windows
def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:
        st.warning("Sound alert only works on Windows with winsound.")

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"

# Streamlit UI
st.title("Countdown Timer")

seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)
start = st.button("Start Countdown")

if start:
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(seconds, 0, -1):
        status_text.write(f"Time left: {format_time(i)}")
        progress_bar.progress((seconds - i + 1) / seconds)
        time.sleep(1)

    status_text.write("Time's up!")
    play_sound()
