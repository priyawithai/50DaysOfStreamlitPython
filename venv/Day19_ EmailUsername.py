import streamlit as st

# App Title and Header
st.set_page_config(page_title="Email Username Extractor", page_icon="🆔")
st.title("🆔 Email Username Extractor")
st.markdown("### Day 19 of the #FlyHighwithAI 🦅 Challenge")
st.caption("Enter an email address to extract the username (everything before `@`)")

# Input from user
email = st.text_input("📧 Enter your email address:")

# Function to extract username and domain
def extract_email_parts(email):
    if "@" not in email:
        return None, None
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return None, None
    return parts[0], parts[1]

# Processing logic
if email:
    username, domain = extract_email_parts(email)

    if username:
        st.success(f"🆔 **Username:** `{username}`")
        st.info(f"👋 Welcome back, **{username}**!")
        
        # Bonus feature
        with st.expander("🔍 Show domain part (bonus feature)"):
            st.write(f"🌐 **Domain:** `{domain}`")
    else:
        st.error("⚠️ Please enter a valid email address with an `@` symbol and proper format.")
else:
    st.info("⏳ Waiting for your input...")

# Footer
st.markdown("---")
st.caption("Crafted with 💡 and Streamlit · #FlyHighwithAI 🚀")
