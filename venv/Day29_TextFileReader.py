# TextFileReader.py
import streamlit as st
import string

# App title
st.set_page_config(page_title="Text File Reader 📁", page_icon="📄", layout="centered")
st.title("📄 Text File Reader")
st.subheader("Day 29 — AI Python Challenge 🦅  #FlyHighwithAI")

st.markdown("Upload a `.txt` file to instantly see **lines**, **words**, **characters**, and a **reading time** estimate.")

# File uploader
uploaded_file = st.file_uploader("📂 Choose a .txt file", type=["txt"])

if uploaded_file is not None:
    # Read file
    content = uploaded_file.read().decode("utf-8")
    lines = content.splitlines()

    # Word processing: remove punctuation and split
    translator = str.maketrans("", "", string.punctuation)
    words = content.translate(translator).split()
    total_lines = len(lines)
    total_words = len(words)
    total_chars = len(content)
    
    # Estimate reading time (assuming ~200 words per minute)
    reading_time = total_words / 200
    reading_time_min = max(1, round(reading_time))

    # Preview first few lines
    st.markdown("### 📜 Preview")
    preview_lines = lines[:5] if lines else ["(File is empty)"]
    st.code("\n".join(preview_lines), language="text")

    # Display stats in info cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📄 Total Lines", total_lines)
    col2.metric("✍️ Total Words", total_words)
    col3.metric("🔡 Characters", total_chars)
    col4.metric("⏳ Reading Time", f"{reading_time_min} min")

else:
    st.info("⬆️ Upload a `.txt` file to get started.")
