import streamlit as st
import time

# Page Config
st.set_page_config(page_title="🧮 Sum Calculator - #FlyHighwithAI", page_icon="🦅", layout="centered")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 9: Sum Calculator</h1>
    <p style='text-align: center; font-size: 18px;'>Fly high with loops! Let's calculate the sum from <b>1 to n</b> and watch the loop in action! 🚀</p>
""", unsafe_allow_html=True)

# Input section
n = st.number_input("Enter a number (1 - 10,000):", min_value=1, max_value=10000, step=1)

# Toggle for live loop view
show_live = st.checkbox("🔁 Show live loop animation", value=True)
show_breakdown = st.checkbox("📊 Show summation breakdown")

# Sum Calculation
if st.button("🚀 Calculate Sum"):
    total = 0
    progress_bar = st.progress(0)
    status_text = st.empty()
    breakdown = ""

    for i in range(1, n + 1):
        total += i
        if show_breakdown:
            breakdown += f"{i} + " if i < n else f"{i}"
        if show_live:
            status_text.markdown(f"<span style='color: #006400;'>Adding {i} → Current Sum: {total}</span>", unsafe_allow_html=True)
            progress_bar.progress(i / n)
            time.sleep(0.001 if n < 1000 else 0)  # Faster for large n

    st.balloons()
    st.success(f"🎉 The sum of numbers from 1 to {n} is: **{total}**")

    if show_breakdown and n <= 200:
        st.markdown(f"<p style='color: #8B0000; font-weight: bold;'>Summation:</p> <code>{breakdown} = {total}</code>", unsafe_allow_html=True)
    elif show_breakdown:
        st.info("⚠️ Breakdown hidden for large numbers (over 200) to keep the app fast.")

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size: 16px;'>🔥 Challenge by #FlyHighwithAI | Day 9 Complete! | Crafted with ❤️ and 🐍</p>
""", unsafe_allow_html=True)
