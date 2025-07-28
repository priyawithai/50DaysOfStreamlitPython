import streamlit as st
import math

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="🔍 Number Checker",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Number Checker")
st.markdown("Welcome to **Day 23** of the **AI Python Challenge** 🦅 — let’s explore numbers together with logic and fun! #FlyHighwithAI 💡")

st.divider()

# ---------------------------
# Input Section
# ---------------------------
number = st.number_input("🔢 Enter an integer to analyze", value=0, step=1, format="%d")

# ---------------------------
# Toggle for Detailed Output
# ---------------------------
detailed = st.toggle("🧠 Show detailed explanations", value=True)

# ---------------------------
# Functions for Checking
# ---------------------------
def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ---------------------------
# Result Output
# ---------------------------
st.header("📊 Results")

# Check 1: Positive or Negative
if number > 0:
    st.success("✅ The number is Positive 🔼")
    if detailed:
        st.info("ℹ️ A positive number is greater than 0.")
elif number < 0:
    st.error("❌ The number is Negative 🔽")
    if detailed:
        st.info("ℹ️ A negative number is less than 0.")
else:
    st.warning("🟡 The number is Zero")
    if detailed:
        st.info("ℹ️ Zero is neither positive nor negative.")

# Check 2: Even or Odd
if is_even(number):
    st.success("✅ The number is Even ⚖️")
    if detailed:
        st.info("ℹ️ Even numbers are divisible by 2 (e.g., 2, 4, 6).")
else:
    st.error("❌ The number is Odd 🎲")
    if detailed:
        st.info("ℹ️ Odd numbers are not divisible by 2 (e.g., 1, 3, 5).")

# Check 3: Prime or Not
if is_prime(number):
    st.success("✅ The number is Prime 🔍")
    if detailed:
        st.info(f"ℹ️ {number} is only divisible by 1 and itself — that's what makes it prime.")
else:
    st.error("❌ The number is Not Prime 🧩")
    if detailed:
        if number < 2:
            st.info("ℹ️ Prime numbers must be greater than 1.")
        else:
            st.info(f"ℹ️ {number} has divisors other than 1 and itself, so it is not prime.")

# ---------------------------
# Footer
# ---------------------------
st.divider()
st.markdown("✅ Explore logic. 💡 Learn patterns. 🎯 Keep flying high, Eagles! #Day23 #AIChallenge #FlyHighwithAI")
