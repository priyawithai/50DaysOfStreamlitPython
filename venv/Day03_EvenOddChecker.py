import streamlit as st
import time
import random

# --- Page Config ---
st.set_page_config(page_title="Even or Odd WOW Checker", page_icon="✨", layout="centered")

# --- Custom CSS for animations & effects ---
st.markdown("""
    <style>
        .title {
            font-size: 3em; font-weight: bold; text-align: center; color: #7B2CBF;
            animation: floatIn 2s ease-in-out;
        }
        @keyframes floatIn {
            0% {opacity: 0; transform: translateY(-20px);}
            100% {opacity: 1; transform: translateY(0);}
        }
        .result-box {
            background-color: #FFF9C4;
            color: #333;
            padding: 20px;
            border-radius: 10px;
            font-size: 1.2em;
            line-height: 2;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .badge {
            margin-top: 30px;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            background-color: #E3F2FD;
            color: #01579B;
            border-radius: 12px;
            animation: bounce 1.2s infinite;
        }
        @keyframes bounce {
            0%, 100% {transform: translateY(0);}
            50% {transform: translateY(-8px);}
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title'>✨ Even-Odd Intelligence Checker</div>", unsafe_allow_html=True)
st.caption("🚀 Day 3 of 50 – #FlyHighwithAI 🦅 | Designed to surprise & delight.")

st.divider()

# --- Single Number Input ---
st.subheader("🔍 Solo Number Test")
single = st.text_input("Type a number and see what it says 👇", key="solo")

def playful_response(n: int):
    label = "Even" if n % 2 == 0 else "Odd"
    emoji = "✅" if label == "Even" else "🌀"
    return f"🗣️ I am **{n}**, and I'm **{label}**! {emoji}"

if single.strip():
    if single.strip().lstrip("-").isdigit():
        num = int(single)
        time.sleep(0.5)
        st.success(playful_response(num))
    else:
        st.error("⛔ Please enter a valid number!")

# --- List Checker ---
st.subheader("📥 Multi-Number Intelligence")
list_input = st.text_area("Paste numbers separated by commas (e.g., 14,17,22):", height=100)

def parse_list(input_str):
    return [int(i.strip()) for i in input_str.replace("(", "").replace(")", "").split(",") if i.strip().lstrip("-").isdigit()]

if st.button("💫 Run AI Check"):
    if list_input.strip():
        try:
            numbers = parse_list(list_input)
            evens = 0
            odds = 0
            animated_lines = []

            st.info("🔮 Thinking like an AI...")
            progress = st.progress(0)

            for idx, n in enumerate(numbers):
                time.sleep(0.1)
                label = "Even" if n % 2 == 0 else "Odd"
                emoji = "✅" if label == "Even" else "🌀"
                animated_lines.append(f"🤖 {n} says: I am {label}! {emoji}")
                if label == "Even": evens += 1
                else: odds += 1
                progress.progress((idx + 1) / len(numbers))

            # Confetti Emoji Rain 🎊🎊🎊
            st.markdown("<div class='result-box'>" + "<br>".join(animated_lines) + "</div>", unsafe_allow_html=True)
            st.markdown("<div class='badge'>🎯 Final Result: <br> "
                        f"{evens} Even 🔵 & {odds} Odd 🟠 in your list!</div>", unsafe_allow_html=True)
            
            # Confetti Effect with Emojis
            confetti_emojis = random.choices(["🎉", "✨", "🌟", "🎊", "💫"], k=30)
            st.markdown(f"<center style='font-size: 2em'>{''.join(confetti_emojis)}</center>", unsafe_allow_html=True)

        except Exception as e:
            st.error("⚠️ Input error. Please only enter integers.")
    else:
        st.warning("📌 Enter a list before checking!")

# --- Footer ---
st.markdown("<br><div style='background:#E0F7FA; padding:12px; border-radius:10px; text-align:center; color:#006064'>"
            "🧠 Day 3 Complete – You just added intelligence to numbers! See you on Day 4, Eagle 🦅"
            "</div>", unsafe_allow_html=True)
