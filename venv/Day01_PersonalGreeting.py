# PersonalGreeting.py

import streamlit as st
from difflib import get_close_matches

# --- AI Description Generator ---
def generate_ai_description(name, color, age):
    traits = {
        'red': 'bold and unstoppable',
        'blue': 'calm and visionary',
        'green': 'balanced and nurturing',
        'yellow': 'bright and curious',
        'white': 'pure and imaginative',
        'black': 'mysterious and powerful',
        'purple': 'wise and creative',
        'pink': 'joyful and kind',
        'orange': 'energetic and inventive'
    }

    user_color = color.lower()
    valid_colors = list(traits.keys())
    closest_match = get_close_matches(user_color, valid_colors, n=1)

    if user_color in traits:
        aura = traits[user_color]
    elif closest_match:
        aura = traits[closest_match[0]]
        st.info(f"🎨 Interpreted your color as **{closest_match[0]}** for aura generation.")
    else:
        aura = "uniquely brilliant"
        st.warning("✨ We couldn't match your color exactly, but we've assigned a special AI aura for you!")

    return f"{name} radiates a {aura} energy at age {age} 🚀"

# --- Aura Score Calculator ---
def calculate_aura_score(color, age):
    return (sum(ord(c) for c in color.lower()) + age * 3) % 100

# --- Aura Score Meaning Map ---
def get_aura_meaning(score):
    if score <= 20:
        return "Mysterious Dreamer ✨", "🌀🌙🧘‍♀️"
    elif score <= 40:
        return "Deep Thinker, Soft Energy 🧠", "📘☁️🦉"
    elif score <= 60:
        return "Balanced Explorer 🌱", "🌿🚀😌"
    elif score <= 80:
        return "Radiant Creator 🔥", "🎨⚡️💫"
    else:
        return "Cosmic Visionary 🚀", "🌈🌟👑"

# --- Streamlit App UI ---
st.set_page_config(page_title="Hello Eagles! 🦅 | Day 1", page_icon="🦅", layout="centered")

st.markdown("<h1 style='text-align: center;'>🦅 Hello Eagles! Day 1 of 50</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6c63ff;'>Let's create your AI-powered Personal Greeting ✨</h3>", unsafe_allow_html=True)
st.divider()

# User Inputs
name = st.text_input("👤 Enter your name:")
age = st.number_input("🎂 Enter your age:", min_value=1, max_value=120, step=1)
color = st.text_input("🎨 What's your favorite color?")

if st.button("Generate My Greeting 🚀"):
    if name and age and color:
        aura_score = calculate_aura_score(color, age)
        description = generate_ai_description(name, color, age)
        meaning, emojis = get_aura_meaning(aura_score)

        # Set text color safely
        safe_color = color.lower() if color.lower() != "white" else "#333333"

        st.markdown(f"<h2 style='color:{safe_color}'>👋 Hey {name}!</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px;'>You are {age} years young and your aura shines in <b>{color}</b>!</p>", unsafe_allow_html=True)
        st.success(f"✨ {description}")

        st.markdown(f"<h4>🔮 Your AI Aura Score: <span style='color:#ff4b4b'>{aura_score}/100</span></h4>", unsafe_allow_html=True)
        st.info(f"🧬 **Aura Meaning:** *{meaning}* {emojis}")

        st.balloons()
    else:
        st.warning("Please fill in all fields to receive your magical greeting!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>#FlyHighwithAI ✨ | Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
