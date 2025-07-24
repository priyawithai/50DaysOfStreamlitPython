import streamlit as st
import time
import random

# --- Page Config ---
st.set_page_config(page_title="🔢 Number Comparison | FlyHighwithAI", page_icon="🦅", layout="centered")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        body {background-color: #f5f7fa;}
        .result-box {
            padding: 1rem;
            border-radius: 1rem;
            background-color: #ffffff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            font-size: 24px;
            color: #333333;
            margin-top: 1.5rem;
        }
        .ai-meter {
            font-size: 18px;
            color: #555;
            margin-top: 10px;
        }
        .ai-avatar {
            font-size: 20px;
            margin-top: 1.5rem;
            background-color: #e0e7ff;
            padding: 10px;
            border-radius: 10px;
            border-left: 6px solid #6366f1;
            color: #1f2937; /* Darker text for visibility */
        }
        .quote-box {
            font-size: 16px;
            font-style: italic;
            color: #6b7280;
            margin-top: 1rem;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 6: Number Comparison Tool</h1>
    <p style='text-align: center; font-size: 18px;'>Welcome to the #FlyHighwithAI Challenge! Let's compare two numbers with style, smarts, and a sprinkle of AI magic. ✨</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("🔢 Enter First Number", key="num1", value=0)

with col2:
    num2 = st.number_input("🔢 Enter Second Number", key="num2", value=0)

# --- Fun Quotes ---
quotes = [
    "“Numbers never lie, but AI makes them smile!” 😄",
    "“Sometimes even digits have drama!” 🎭",
    "“Keep flying high, even if your number's low!” 🛫",
    "“Comparison is the thief of joy… unless it’s fun like this!” 🤹‍♂️"
]

# --- AI Avatar Messages ---
avatars = {
    "greater": "🧠 Captain Compare: A clear victory for Number 1! 🚀",
    "less": "🤖 AI Buddy: Number 2 takes the crown! 👑",
    "equal": "✨ Peace Maker Bot: Perfect balance. Equality wins! 🤝"
}

# --- Button Logic ---
if st.button("🚀 Compare Now", use_container_width=True):
    st.info("Analyzing with AI precision... Hold tight! ⏳")
    time.sleep(1.5)

    result = ""
    badge = ""
    avatar = ""
    confidence = 0
    quote = random.choice(quotes)

    if num1 > num2:
        result = f"🔺 {num1} is greater than {num2}"
        badge = "🏆 Victory for Number 1!"
        avatar = avatars["greater"]
        confidence = 95
    elif num1 < num2:
        result = f"🔻 {num1} is less than {num2}"
        badge = "📉 Number 2 wins this round!"
        avatar = avatars["less"]
        confidence = 95
    else:
        result = f"✅ Both numbers are equal: {num1} = {num2}"
        badge = "🤝 Equality Achieved!"
        avatar = avatars["equal"]
        confidence = 100

    # Simulate AI thinking
    with st.spinner("Crunching numbers with AI energy... ⚡"):
        time.sleep(1.2)

    # --- Display Results ---
    st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
    st.success(badge)

    st.markdown(f"<div class='ai-avatar'>{avatar}</div>", unsafe_allow_html=True)

    st.progress(confidence / 100, text="AI Confidence Meter 📊")

    st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)

    # --- Animation ---
    if num1 == num2:
        st.balloons()
    else:
        st.snow()

# --- Footer ---
st.markdown("---")
st.caption("✨ Built with ❤️ by your friendly AI on Day 6 of the #FlyHighwithAI Challenge 🦅")
