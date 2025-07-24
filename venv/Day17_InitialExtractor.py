import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Initial Extractor", page_icon="🆔", layout="centered")

# --- Title ---
st.title("🆔 Initial Extractor")
st.subheader("Turn full names into crisp initials — fast and clean!")
st.markdown("**#FlyHighwithAI 🚀 | Day 17 of the AI Python Challenge 🦅**")

# --- Input ---
full_name = st.text_input("Enter Full Name", placeholder="e.g. John Doe Smith")

# --- Style Toggle ---
style = st.radio(
    "Choose Initial Format:",
    options=["With dots (J.D.S.)", "Without dots (JDS)", "Lowercase (jds)"],
    horizontal=True
)

# --- Extract Initials Function ---
def extract_initials(name, style="With dots (J.D.S.)"):
    # Clean and split the name
    parts = name.strip().split()
    if not parts:
        return ""
    
    initials = [part[0] for part in parts if part]
    
    if style == "With dots (J.D.S.)":
        return '.'.join([i.upper() for i in initials]) + '.'
    elif style == "Without dots (JDS)":
        return ''.join([i.upper() for i in initials])
    elif style == "Lowercase (jds)":
        return ''.join([i.lower() for i in initials])
    else:
        return ""

# --- Output ---
if full_name:
    initials = extract_initials(full_name, style)
    
    st.success("✅ Initials Extracted!")
    st.markdown(f"**Original Name:** {full_name}")
    st.markdown(f"**Extracted Initials:** `{initials}`")
    
    # Copy button
    st.code(initials, language="text")
    st.button("📋 Copy to Clipboard", help="(Use your mouse or keyboard shortcut to copy above!)")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | #Day17 #InitialExtractor #FlyHighwithAI 🦅")
