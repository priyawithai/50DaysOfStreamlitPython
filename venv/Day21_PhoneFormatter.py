import streamlit as st
import re

st.set_page_config(page_title="📞 Phone Number Formatter", page_icon="📱")

st.title("📞 Phone Number Formatter")
st.subheader("Day 21 - AI Python Challenge 🦅")
st.markdown("Transform your 10-digit number into a clean **(XXX) XXX-XXXX** format. Instant. Stylish. Smart. 💡")

# Input field
user_input = st.text_input("Enter a 10-digit phone number (digits only)", max_chars=20, placeholder="e.g., 9876543210")

# Helper functions
def clean_number(raw):
    return re.sub(r'\D', '', raw)

def format_number(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

# Validation and display logic
if user_input:
    if not re.fullmatch(r'[\d\s\-\(\)]*', user_input):
        st.error("❌ Invalid characters found. Please use only digits, spaces, dashes (-), or parentheses ().")
    else:
        digits = clean_number(user_input)
        if len(digits) < 10:
            st.warning("⚠️ Number is too short. Please enter exactly 10 digits.")
        elif len(digits) > 10:
            st.warning("⚠️ Number is too long. Please enter exactly 10 digits.")
        else:
            formatted = format_number(digits)
            with st.container():
                st.success("✅ Valid number formatted below:")
                st.markdown(f"""
                    <h3 style='color:#4CAF50; font-size: 28px;'>📞 {formatted}</h3>
                """, unsafe_allow_html=True)
            st.button("📋 Copy to Clipboard", on_click=lambda: st.toast("Copied to clipboard! (Just pretend 😉)"))

# Explanation section
with st.expander("🛠 How This Works"):
    st.markdown("""
    - We **validate** that the input includes only digits and common separators (spaces, dashes, parentheses).
    - We **strip out** all non-digit characters using regex.
    - If we get exactly **10 digits**, we format them as **(XXX) XXX-XXXX** for clarity and polish.
    """)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit • #FlyHighwithAI 🚀")
