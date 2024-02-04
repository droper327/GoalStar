import streamlit as st
import time

# Set the page configuration
st.set_page_config(
    page_title="Goal Tracker & Alarm",
    page_icon="✅",
    layout="wide"
)

# Display the current time
current_time = time.strftime("%H:%M:%S")
st.title("Welcome to Your Goal Tracker & Alarm")
st.subheader(f"Current Time: {current_time}")

# Input for setting an alarm
alarm_time = st.time_input("Set an Alarm Time", value=time.strptime("08:00", "%H:%M"))
if alarm_time:
    st.success(f"Alarm set for {alarm_time.tm_hour:02d}:{alarm_time.tm_min:02d}")

# Daily goal checklist
st.header("Daily Goals")
goals = st.text_area("Enter your goals (one per line)", height=150)
if goals:
    goal_list = goals.split("\n")
    st.success(f"Goals added: {len(goal_list)}")

# Goal checkpoints
st.header("Goal Checkpoints")
if st.button("Check Progress"):
    # Simulate checking progress (you can customize this logic)
    completed_goals = ["Exercise", "Read", "Write"]
    st.success(f"Completed goals: {', '.join(completed_goals)}")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Copilot")

# Run the app
if __name__ == "__main__":
    st.run()
