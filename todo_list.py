import streamlit as st
import os

TASKS_FILE = "tasks.txt"

# Load and Save Functions
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                name, completed, priority = line.strip().split(" | ")
                tasks.append({"name": name, "completed": completed == "True", "priority": priority})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['name']} | {task['completed']} | {task['priority']}\n")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

# UI Components
st.title("To-Do List App (Streamlit Edition)")

menu = st.sidebar.selectbox("Menu", ["View Tasks", "Add Task", "Edit Task", "Mark Complete", "Remove Task"])

# Display Tasks
def display_tasks(completed=False):
    tasks = [t for t in st.session_state.tasks if t["completed"] == completed]
    if not tasks:
        st.info("No tasks here.")
        return
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order[x["priority"]])
    for i, task in enumerate(tasks):
        st.write(f"**{i+1}. {task['name']}** (Priority: {task['priority']})")

# View Tasks
if menu == "View Tasks":
    st.subheader("Pending Tasks")
    display_tasks(False)

    st.subheader("Completed Tasks")
    display_tasks(True)

# Add Task
elif menu == "Add Task":
    st.subheader("Add a New Task")
    name = st.text_input("Task Name")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    if st.button("Add Task"):
        if name.strip() != "":
            st.session_state.tasks.append({"name": name, "completed": False, "priority": priority})
            save_tasks(st.session_state.tasks)
            st.success("Task added!")

# Edit Task
elif menu == "Edit Task":
    st.subheader("Edit a Task")
    editable_tasks = [t for t in st.session_state.tasks if not t["completed"]]
    task_names = [f"{i+1}. {t['name']}" for i, t in enumerate(editable_tasks)]

    if editable_tasks:
        selected = st.selectbox("Select task to edit", task_names)
        idx = task_names.index(selected)
        new_name = st.text_input("New Name", editable_tasks[idx]["name"])
        new_priority = st.selectbox("New Priority", ["High", "Medium", "Low"], index=["High", "Medium", "Low"].index(editable_tasks[idx]["priority"]))

        if st.button("Update Task"):
            editable_tasks[idx]["name"] = new_name
            editable_tasks[idx]["priority"] = new_priority
            save_tasks(st.session_state.tasks)
            st.success("Task updated!")
    else:
        st.info("No pending tasks to edit.")

# Mark Task Complete
elif menu == "Mark Complete":
    st.subheader("Mark a Task as Complete")
    pending_tasks = [t for t in st.session_state.tasks if not t["completed"]]
    task_names = [f"{i+1}. {t['name']}" for i, t in enumerate(pending_tasks)]

    if pending_tasks:
        selected = st.selectbox("Select task", task_names)
        idx = task_names.index(selected)
        if st.button("Mark as Completed"):
            pending_tasks[idx]["completed"] = True
            save_tasks(st.session_state.tasks)
            st.success("Marked as completed!")
    else:
        st.info("No pending tasks to complete.")

# Remove Task
elif menu == "Remove Task":
    st.subheader("Remove a Task")
    all_tasks = st.session_state.tasks
    task_names = [f"{i+1}. {t['name']} (Done)" if t["completed"] else f"{i+1}. {t['name']}" for i, t in enumerate(all_tasks)]

    if all_tasks:
        selected = st.selectbox("Select task to remove", task_names)
        idx = task_names.index(selected)
        if st.button("Delete Task"):
            removed = st.session_state.tasks.pop(idx)
            save_tasks(st.session_state.tasks)
            st.success(f"Deleted: {removed['name']}")
    else:
        st.info("No tasks to remove.")
