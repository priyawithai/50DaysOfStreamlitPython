# CountdownTimer.py
import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="⏳ Countdown Timer", page_icon="🚀", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .big-number {
        font-size: 100px;
        font-weight: bold;
        text-align: center;
        color: #FF4500;
    }
    .title-text {
        text-align: center;
        color: #4B0082;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Header ---
st.markdown("<h1 class='title-text'>🦅 Day 12: Countdown Timer</h1>", unsafe_allow_html=True)
st.markdown("<p class='title-text'>Ready for liftoff? Hit the button and watch the countdown ignite! 🚀</p>", unsafe_allow_html=True)

# --- Input Section ---
start_num = st.number_input("Choose starting number for countdown (default is 10):", min_value=1, max_value=100, value=10, step=1)

# --- Start Countdown Button ---
if st.button("🔥 Start Countdown", type="primary"):
    countdown_spot = st.empty()  # Placeholder for live countdown

    for i in range(start_num, -1, -1):
        countdown_spot.markdown(f"<div class='big-number'>{i}</div>", unsafe_allow_html=True)
        time.sleep(1)

    st.success("🎉 Countdown Complete! Lift-off! #FlyHighwithAI 🚀")
    st.balloons()

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>Powered by the #FlyHighwithAI Challenge 🦅</p>", unsafe_allow_html=True)
