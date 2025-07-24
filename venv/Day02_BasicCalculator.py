# Day02_BasicCalculator.py
import streamlit as st
import time
import random

# -------------------- Page Config --------------------
st.set_page_config(page_title="🧮 AI-Powered Calculator", page_icon="✨", layout="centered")

# -------------------- Session State for History --------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------- Custom Style (Gradient + Components) --------------------
st.markdown("""
    <style>
        body, .stApp {
            background: linear-gradient(135deg, #f0f9ff, #e0f7fa, #fce7f3);
            background-size: 400% 400%;
            animation: gradientFlow 15s ease infinite;
        }

        @keyframes gradientFlow {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .stButton button {
            background-color: #4f46e5;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 2em;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background-color: #4338ca;
            transform: scale(1.05);
        }

        @keyframes shimmer {
            0% { opacity: 0.8; }
            50% { opacity: 1; }
            100% { opacity: 0.8; }
        }

        .result-box {
            font-size: 2em;
            font-weight: bold;
            padding: 15px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
            animation: shimmer 2s infinite;
        }

        .quote-box {
            margin-top: 30px;
            padding: 15px;
            background-color: #fff7ed;
            border-left: 6px solid #fb923c;
            border-radius: 10px;
            font-size: 16px;
            color: #7c2d12;
        }

        .history-box {
            margin-top: 30px;
            background-color: #f1f5f9;
            padding: 10px 20px;
            border-radius: 10px;
        }

        .history-title {
            font-weight: bold;
            font-size: 18px;
            color: #1e293b;
        }

        .history-item {
            color: #334155;
            padding: 5px 0;
            font-family: monospace;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------
st.markdown("<h2 style='color:#1e3a8a; text-align:center;'>🧮 Futuristic AI Calculator</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#374151; text-align:center;'>✨ Day 2 of 50 - #FlyHighwithAI | Created with ❤️ by your AI co-pilot</p>", unsafe_allow_html=True)

# -------------------- Input Section --------------------
num1 = st.number_input("🔢 Enter first number", format="%.2f", step=1.0)
num2 = st.number_input("🔢 Enter second number", format="%.2f", step=1.0)

operation = st.radio("🎯 Choose an Operation", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"])

# -------------------- Quotes --------------------
quotes = [
    "📐 Math: The only place where people buy 60 watermelons and no one wonders why.",
    "🧠 Life is complex — it has real and imaginary parts.",
    "💫 Without geometry, life is pointless.",
    "🚀 The limit does not exist... just like your worries after calculating!",
    "📊 Math teachers have too many problems.",
    "🤖 Be rational. Get real. Stay positive!"
]

# -------------------- Calculator Logic --------------------
def calculate(n1, n2, op):
    if op == "➕ Add":
        return n1 + n2
    elif op == "➖ Subtract":
        return n1 - n2
    elif op == "✖️ Multiply":
        return n1 * n2
    elif op == "➗ Divide":
        if n2 == 0:
            return "❌ Cannot divide by zero!"
        return n1 / n2

# -------------------- Calculate Button --------------------
if st.button("✨ Let the AI Calculate"):
    with st.spinner("🧠 AI crunching the numbers..."):
        for percent in range(0, 101, 10):
            st.progress(percent)
            time.sleep(0.1)

    result = calculate(num1, num2, operation)

    # Display Result
    if isinstance(result, (int, float)):
        if result > 0:
            bg_color = "#d1fae5"  # green
            st.snow()
        elif result < 0:
            bg_color = "#fee2e2"  # red
        else:
            bg_color = "#e0e7ff"  # blue

        st.markdown(f"""
            <div class="result-box" style="background-color:{bg_color}; color:#111827;">
                🔍 Result: {round(result, 2)}
            </div>
        """, unsafe_allow_html=True)

        # Add to session history
        expression = f"{num1} {operation[1:]} {num2} = {round(result, 2)}"
        st.session_state.history.append(expression)

    else:
        st.error(result)

    # Quote Box
    quote = random.choice(quotes)
    st.markdown(f"""
        <div class="quote-box">
            💬 {quote}
        </div>
    """, unsafe_allow_html=True)

# -------------------- History Section --------------------
if st.session_state.history:
    st.markdown("<div class='history-box'>", unsafe_allow_html=True)
    st.markdown("<div class='history-title'>📚 Calculation History</div>", unsafe_allow_html=True)
    for item in reversed(st.session_state.history[-5:]):
        st.markdown(f"<div class='history-item'>• {item}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
