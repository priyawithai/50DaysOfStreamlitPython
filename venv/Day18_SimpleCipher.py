import streamlit as st

# -----------------------------
# Simple Caesar Cipher Function
# -----------------------------
def shift_text(text, shift, mode='encode'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encode' else -shift
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="🔐 Simple Cipher", page_icon="🔐", layout="centered")

st.title("🔐 Simple Caesar Cipher Playground")
st.markdown("Welcome to your encryption zone, Agent 🧠. Here, you can **encode** or **decode** secret messages with a Caesar cipher. Shift letters and uncover mysteries. ✉️")

st.subheader("✍️ Enter your message")
user_input = st.text_area("Message", placeholder="Type your secret message here...", height=150)

col1, col2 = st.columns(2)

with col1:
    shift_amount = st.slider("🔁 Shift amount", min_value=1, max_value=25, value=1)
with col2:
    mode = st.radio("🧭 Mode", ["encode", "decode"], index=0, horizontal=True)

# Encode/Decode Logic
if user_input:
    output = shift_text(user_input, shift_amount, mode)

    st.subheader("🔓 Output")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**Original Message**")
        st.code(user_input, language="text")
    with col4:
        st.markdown(f"**{'Encoded' if mode == 'encode' else 'Decoded'} Message**")
        st.code(output, language="text")
else:
    st.info("Enter a message above to get started!")

# -----------------------------
# Fun Explanation Section
# -----------------------------
with st.expander("📘 How does this work?"):
    st.markdown("""
    - This is a **Caesar Cipher**, one of the oldest encryption techniques. 🔐  
    - Each **letter is shifted** by a number you choose (e.g., shift 1: `a → b`, `z → a`).  
    - The cipher wraps around the alphabet and keeps **uppercase/lowercase intact**.  
    - Non-alphabet characters like `@`, `!`, and spaces are **unchanged**.  
    - Great for secret notes, puzzles, or just learning how encryption works! 🧠
    """)

st.markdown("---")
st.markdown("Made with ❤️ for the **AI Python Challenge - Day 18** 🦅 | #FlyHighwithAI 🚀")
