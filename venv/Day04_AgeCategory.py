import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Day 4 - Age Category", page_icon="🦅", layout="centered")

# Custom Title (Your Markdown)
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 4: Age Category Classifier</h1>
    <p style='text-align: center; font-size: 18px;'>Welcome to the #FlyHighwithAI Challenge – let's see where your age places you in this colorful journey of life! ✨</p>
""", unsafe_allow_html=True)
st.markdown("---")

# Age Input
age = st.number_input("🔵 Enter your age:", min_value=0, max_value=120, step=1)

# Age Classification Logic
if age:
    if age <= 12:
        category = "Child"
        message = "You're in the age of wonder, curiosity, and play!"
        emoji = "🎈"
        wisdom = random.randint(10, 30)
        wow_item = "May your laughter be endless and your dreams big! 🌈"
        bg_color = "#fff1f2"
    elif 13 <= age <= 19:
        category = "Teenager"
        message = "You're exploring your identity and shaping your future!"
        emoji = "🎧"
        wisdom = random.randint(30, 50)
        wow_item = "Keep believing in yourself and chase the stars! 🚀"
        bg_color = "#f3e8ff"
    elif 20 <= age <= 59:
        category = "Adult"
        message = "You’re navigating life with strength and ambition!"
        emoji = "💼"
        wisdom = random.randint(50, 80)
        wow_item = "You’ve got this — and you’re still growing! 💪"
        bg_color = "#ffe4e6"
    else:
        category = "Senior"
        message = "Your wisdom is your superpower!"
        emoji = "🌿"
        wisdom = random.randint(80, 100)
        wow_item = "Your journey inspires generations! 🌟"
        bg_color = "#fef3c7"

    # Output Display Box
    st.markdown(f"""
        <div style="
            background-color: {bg_color};
            padding: 20px;
            border-radius: 12px;
            color: #000000;
        ">
            <h2 style="margin-bottom: 10px; color: red;">
                <strong>{emoji} You are a {category}!</strong>
            </h2>
            <p style="font-size: 18px; margin: 5px 0;">{message}</p>
            <p style="font-style: italic; font-size: 16px; margin-top: 10px;">✨ {wow_item}</p>
        </div>
    """, unsafe_allow_html=True)

    # Wisdom Score Display
    st.markdown("### 🧠 Wisdom Score")
    st.progress(wisdom / 100)

    # Wisdom Score Meaning
    with st.expander("💡 What is Wisdom Score?"):
        st.write("""
        The **Wisdom Score** is a playful way to represent how much life experience you might have gathered based on your age.

        - 🟢 0–30: You're just starting your journey. Endless curiosity and wonder!
        - 🟡 31–70: You're shaping your future and building experiences.
        - 🔴 71–100: You're a beacon of life lessons and deep understanding!

        It's not scientific — it's motivational! 💡
        """)

# Footer
st.markdown("---")
st.caption("🚀 Powered by Streamlit · #FlyHighwithAI ✨")
