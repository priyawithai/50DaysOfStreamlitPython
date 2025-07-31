# MathOperations.py
import streamlit as st
import math

# App title and intro
st.set_page_config(page_title="Math Operations Calculator 🧮", layout="centered")
st.title("🧮 Math Operations Calculator")
st.caption("Welcome to Day 25 of the AI Python Challenge 🦅")
st.markdown("**#FlyHighwithAI 💡** — Make Math Simple, Smart & Interactive")

# Operation selection
operation = st.selectbox("Select a Math Operation ➗", ["Factorial (n!)", "Power (a^b)", "Square Root (√n)"])

st.divider()

# Factorial Function
def compute_factorial(n):
    return math.factorial(n)

# Power Function
def compute_power(base, exponent):
    return math.pow(base, exponent)

# Square Root Function
def compute_sqrt(n):
    return math.sqrt(n)

# Dynamic input handling
if operation == "Factorial (n!)":
    st.subheader("✨ Factorial Operation")
    num = st.number_input("Enter a non-negative integer (n):", min_value=0, step=1, format="%d")
    if st.button("Calculate Factorial"):
        result = compute_factorial(int(num))
        st.success(f"✅ Result: {int(num)}! = {result}")
        st.info("🧠 Formula: n! = n × (n-1) × (n-2) × ... × 1")

elif operation == "Power (a^b)":
    st.subheader("✨ Power Operation")
    base = st.number_input("Enter the base (a):")
    exponent = st.number_input("Enter the exponent (b):")
    if st.button("Calculate Power"):
        result = compute_power(base, exponent)
        st.success(f"✅ Result: {base} ^ {exponent} = {result}")
        st.info("🧠 Formula: a^b = a × a × ... (b times)")

elif operation == "Square Root (√n)":
    st.subheader("✨ Square Root Operation")
    num = st.number_input("Enter a non-negative number (n):", min_value=0.0)
    if st.button("Calculate Square Root"):
        result = compute_sqrt(num)
        st.success(f"✅ Result: √{num} = {result}")
        st.info("🧠 Formula: √n = a number which when squared gives n")

# Footer
st.divider()
st.caption("Created with ❤️ by AI Python Challenge Team | Day 25/50")
