import streamlit as st

# Define questions and answers
questions = {
        "What is the capital of France?": {
            "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
            "answer": "a"
        },
        "Which language is used for web development?": {
            "options": ["a) Python", "b) JavaScript", "c) Java", "d) C++"],
            "answer": "b"
        },
        "What does CPU stand for?": {
            "options": ["a) Central Processing Unit", "b) Computer Personal Unit", "c) Central Personal Unit", "d) Computer Processing Unit"],
            "answer": "a"
        },
        "What is the main Python library for data analysis?": {
            "options": ["a) pandas", "b) numpy", "c) matplotlib", "d) scikit-learn"],
            "answer": "a"
        }, 
        "Which Python library is used for numerical computations?": {
            "options": ["a) pandas", "b) numpy", "c) matplotlib", "d) seaborn"],
            "answer": "b"
        },
        "What type of plot is used to show data distribution?": {
            "options": ["a) line plot", "b) bar chart", "c) histogram", "d) scatter plot"],
            "answer": "c"
        },
        "What does CSV stand for?": {
            "options": ["a) Comma Separated Values", "b) Comma Semicolon Values", "c) Character Separated Values", "d) Comma Space Values"],
            "answer": "a"
        },
        "What Python library is commonly used for data visualization?": {
            "options": ["a) pandas", "b) matplotlib", "c) numpy", "d) tensorflow"],
            "answer": "b"
        },
        "Which function is used to read a CSV file in pandas?": {
            "options": ["a) read_csv()", "b) read_excel()", "c) read_txt()", "d) open_csv()"],
            "answer": "a"
        },
        "What does NaN stand for in data?": {
            "options": ["a) Not a Number", "b) Number and Name", "c) Null and None", "d) Not a Name"],
            "answer": "a"
        },
        "What is the keyword to define a function in Python?": {
            "options": ["a) func", "b) function", "c) def", "d) define"],
            "answer": "c"
        },
        "Which keyword is used to create a class in Python?": {
            "options": ["a) func", "b) class", "c) def", "d) create"],
            "answer": "b"
        },
        "What is the file extension for a Python file?": {
            "options": ["a) .py", "b) .python", "c) .pt", "d) .txt"],
            "answer": "a"
        },
        "Which keyword is used to handle exceptions?": {
            "options": ["a) catch", "b) except", "c) try", "d) handle"],
            "answer": "c"
        },
        "What is the output of 3 ** 2 in Python?": {
            "options": ["a) 6", "b) 9", "c) 8", "d) 5"],
            "answer": "b"
        },
        "What is the Python keyword for loop iteration?": {
            "options": ["a) loop", "b) while", "c) for", "d) iterate"],
            "answer": "c"
        },
        "What is the output of len('data')?": {
            "options": ["a) 3", "b) 5", "c) 4", "d) 2"],
            "answer": "c"
        },
        "Which data type is used to store True/False values?": {
            "options": ["a) int", "b) string", "c) boolean", "d) float"],
            "answer": "c"
        },
        "Which ML library starts with 'sci'?": {
            "options": ["a) scipy", "b) scikit-learn", "c) scikit-image", "d) sklearn"],
            "answer": "b"
        },
        "What does IDE stand for?": {
            "options": ["a) Integrated Development Environment", "b) Integrated Design Editor", "c) Internal Development Environment", "d) Interactive Debugger Environment"],
            "answer": "a"
        }
    }

# Initialize Streamlit session state variables
if "current" not in st.session_state:
    st.session_state.current = 0  # tracks the current question number
if "score" not in st.session_state:
    st.session_state.score = 0  # tracks the user's score
if "submitted" not in st.session_state:
    st.session_state.submitted = False  # tracks if answer is submitted

# Convert questions dict to list for indexing
question_keys = list(questions.keys())

# Display current question
if st.session_state.current < len(question_keys):
    question = question_keys[st.session_state.current]  # get question text
    q_data = questions[question]  # get options and correct answer

    st.header(f"Question {st.session_state.current + 1}")
    st.write(question)

    # Show options with radio button
    answer = st.radio("Choose your answer:", q_data["options"], key=st.session_state.current)

    # When user clicks "Submit"
    if st.button("Submit"):
        selected = answer[0]  # get the first character (a/b/c/d)
        if selected == q_data["answer"]:
            st.session_state.score += 1
            st.success("Correct!")  # green box for correct
        else:
            correct_option = next(opt for opt in q_data["options"] if opt.startswith(q_data["answer"]))
            st.error(f"Wrong! Correct answer: {correct_option}")  # red box
        st.session_state.submitted = True

    # Show Next button after submission
    if st.session_state.submitted:
        if st.button("Next Question"):
            st.session_state.current += 1
            st.session_state.submitted = False

else:
    # Final score display
    st.success(f"Quiz Completed! Your Score: {st.session_state.score}/{len(questions)}")

    # Restart button
    if st.button("Restart Quiz"):
        st.session_state.current = 0
        st.session_state.score = 0
