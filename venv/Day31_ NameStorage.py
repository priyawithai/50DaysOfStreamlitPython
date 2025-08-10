# NameStorage.py
import streamlit as st
import os

# --- App Config ---
st.set_page_config(page_title="Name Storage 📋", page_icon="📝", layout="centered")
st.title("📝 Name Storage")
st.subheader("Day 31 — AI Python Challenge 🦅  #FlyHighwithAI")

st.markdown("Add names, store them in a file, and see the full list instantly.")

FILE_PATH = "names.txt"

# --- Load existing names ---
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
else:
    names = []

# --- Name Entry ---
new_name = st.text_input("Enter a name:", placeholder="Type a name here...")
if st.button("💾 Save Name"):
    if new_name.strip():
        if new_name.strip() not in names:
            with open(FILE_PATH, "a", encoding="utf-8") as f:
                f.write(new_name.strip() + "\n")
            names.append(new_name.strip())
            st.success(f"✅ '{new_name.strip()}' has been saved!")
        else:
            st.warning(f"⚠️ '{new_name.strip()}' is already in the list.")
    else:
        st.error("❌ Please enter a valid name before saving.")

# --- Clear All ---
if st.button("🗑️ Clear All Names"):
    if os.path.exists(FILE_PATH):
        open(FILE_PATH, "w", encoding="utf-8").close()
    names.clear()
    st.info("📂 All names have been cleared.")

# --- Display Names ---
st.markdown("### 📜 Stored Names")
if names:
    for idx, name in enumerate(names, start=1):
        st.write(f"{idx}. {name}")
else:
    st.write("No names stored yet. Start adding some! 🎉")
