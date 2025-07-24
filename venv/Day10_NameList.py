# NameList.py

import streamlit as st

# --- App Header ---
st.set_page_config(page_title="📝 Name Length Analyzer", page_icon="🦅")
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 10: Name Length Analyzer</h1>
    <p style='text-align: center; font-size: 18px;'>Enter 5 names and discover the personality behind their length! #FlyHighwithAI 🔥</p>
""", unsafe_allow_html=True)

# --- Input Section ---
st.markdown("### ✍️ Enter 5 Names Below")

name_inputs = []
for i in range(1, 6):
    name = st.text_input(f"Name {i}", key=f"name_{i}")
    name_inputs.append(name.strip())

# Filter out empty strings
names = [name for name in name_inputs if name]

# --- Display Section ---
if len(names) == 5:
    name_lengths = {name: len(name) for name in names}

    # Find longest and shortest
    longest_name = max(name_lengths, key=name_lengths.get)
    shortest_name = min(name_lengths, key=name_lengths.get)

    st.markdown("### 📊 Name Lengths Breakdown")
    for name in names:
        length = len(name)
        badge_color = "#2ECC71" if name == longest_name else "#E74C3C" if name == shortest_name else "#3498DB"
        emoji = "📏"
        tag = "🌟 Longest!" if name == longest_name else "🔹 Shortest!" if name == shortest_name else ""
        
        st.markdown(f"""
        <div style='
            background-color:{badge_color};
            color:white;
            padding:12px;
            margin-bottom:10px;
            border-radius:10px;
            font-size:18px;
        '>
            {emoji} <strong>{name}</strong> – 🧠 Length: <strong>{length}</strong> {tag}
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ All 5 names processed successfully!")
else:
    st.info("Please fill in all 5 name fields to see the results.")

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center;'>Built with 💙 by AI • Day 10 of the #FlyHighwithAI Challenge 🦅</p>
""", unsafe_allow_html=True)
