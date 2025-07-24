import streamlit as st
import time

# --- Page Config ---
st.set_page_config(page_title="🔐 Simple Password Checker", page_icon="🛡️", layout="centered")

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 7: Simple Password Checker</h1>
    <p style='text-align: center; font-size: 18px;'>Secure your world, one strong password at a time! 🔐</p>
""", unsafe_allow_html=True)

# --- Password Input ---
password = st.text_input("🔑 Enter your password", type="password")

# --- Password Strength Evaluation ---
def evaluate_password(pw):
    length = len(pw)
    if length == 0:
        return "", 0, "⚪ Please enter a password to check."
    elif length < 8:
        return "🔴 Too short!", 25, "❌ Your password must be at least 8 characters."
    elif length < 12:
        return "🟠 Decent", 60, "✅ Your password is acceptable, but could be stronger."
    elif any(char.isdigit() for char in pw) and any(char.isupper() for char in pw):
        return "🟢 Strong", 90, "🔒 Excellent! Your password is strong and secure."
    else:
        return "🟡 Good", 75, "💡 Add uppercase letters and numbers for extra security."

# --- Suggestion Generator for Decent Passwords ---
def get_suggestions(pw):
    suggestions = []
    if not any(char.isupper() for char in pw):
        suggestions.append("🔸 Add **uppercase letters**")
    if not any(char.isdigit() for char in pw):
        suggestions.append("🔸 Add **numbers**")
    if not any(char in "!@#$%^&*()-_=+[]{};:,.<>?" for char in pw):
        suggestions.append("🔸 Add **special characters** (e.g., @, #, *)")
    if len(pw) < 12:
        suggestions.append("🔸 Increase password length to **12+ characters**")
    return suggestions

# --- Evaluation & Feedback ---
if password:
    status_emoji, confidence, message = evaluate_password(password)

    # --- Progress Bar ---
    st.progress(confidence / 100)

    # --- Feedback Box (Dark Text) ---
    st.markdown(f"""
        <div style='
            margin-top: 20px;
            background-color: #f0f8ff;
            color: #222;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #4B0082;
            font-size: 18px;
        '>
            {status_emoji} <b>Password Confidence:</b> {confidence}%
            <br>📢 <i>{message}</i>
        </div>
    """, unsafe_allow_html=True)

    # --- Suggestions for Decent Passwords ---
    if status_emoji == "🟠 Decent":
        tips = get_suggestions(password)
        if tips:
            st.markdown("### 🛠️ Suggestions to Improve Your Password:")
            for tip in tips:
                st.markdown(f"- {tip}")

    # --- Bonus Tip ---
    st.caption("✨ Tip: Use a mix of uppercase, lowercase, numbers, and symbols for stronger security.")

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>#FlyHighwithAI ✨ | Secure coding made simple.</p>
""", unsafe_allow_html=True)

# --- Balloons for strong password ---
if password and confidence >= 90:
    time.sleep(0.5)
    st.balloons()
