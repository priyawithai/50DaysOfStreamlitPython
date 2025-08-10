# SimpleLog.py
import streamlit as st
from datetime import datetime
import os
import pandas as pd

# --- App Config ---
st.set_page_config(page_title="Simple Log 📓", page_icon="🕒", layout="centered")
st.title("📓 Simple Log")
st.subheader("Day 32 — AI Python Challenge 🦅  #FlyHighwithAI")

st.markdown("Log your daily activities with timestamps and review them anytime.")

FILE_PATH = "log.txt"

# --- Load Existing Logs ---
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        logs = [line.strip() for line in f if line.strip()]
else:
    logs = []

# --- Activity Entry ---
activity = st.text_input("✍️ Enter your activity:", placeholder="e.g., Finished Python project, Went for a run...")
if st.button("💾 Log Activity"):
    if activity.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {activity.strip()}"
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
        logs.insert(0, log_entry)  # latest first in display
        st.success("✅ Activity logged!")
    else:
        st.error("❌ Please enter a valid activity before logging.")

# --- Search Filter ---
search_term = st.text_input("🔍 Search logs:", placeholder="Type to filter...")
filtered_logs = [log for log in logs if search_term.lower() in log.lower()] if search_term else logs

# --- Display Logs ---
st.markdown("### 📜 Logged Activities")
if filtered_logs:
    for log in filtered_logs:
        st.write(log)
else:
    st.info("No matching logs found." if search_term else "No activities logged yet.")

# --- Export Option ---
if logs:
    export_choice = st.selectbox("📤 Export logs as:", ["Select", "TXT", "CSV"])
    if export_choice == "TXT":
        st.download_button(
            label="⬇️ Download TXT",
            data="\n".join(logs),
            file_name="log.txt",
            mime="text/plain"
        )
    elif export_choice == "CSV":
        df = pd.DataFrame([log.split(" - ", 1) for log in logs], columns=["Timestamp", "Activity"])
        st.download_button(
            label="⬇️ Download CSV",
            data=df.to_csv(index=False),
            file_name="log.csv",
            mime="text/csv"
        )
