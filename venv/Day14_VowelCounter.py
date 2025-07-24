import streamlit as st
import re

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(page_title="🔤 Vowel Counter", page_icon="🦅", layout="centered")

# -------------------------------
# Title and Description
# -------------------------------
st.title("🔤 Vowel Counter App")
st.subheader("🦅 Day 14 of the 50-Day AI Python Challenge")
st.markdown("""
Enter any word or sentence below, and this vibrant app will count all the vowels (A, E, I, O, U) — both uppercase and lowercase — and even break them down for you.  
Let’s see how *vocal* your text is! 🔍  
""")

# -------------------------------
# Input Text
# -------------------------------
user_input = st.text_input("✏️ Enter a word or sentence:", "")

# -------------------------------
# Vowel Counting Logic
# -------------------------------
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_counts = {v: 0 for v in vowel_list}
highlighted_text = ""

if user_input:
    total_vowels = 0
    for char in user_input:
        if char.lower() in vowel_list:
            total_vowels += 1
            vowel_counts[char.lower()] += 1
            highlighted_text += f":red[{char}]"
        else:
            highlighted_text += char

    # -------------------------------
    # Output Section
    # -------------------------------
    st.markdown("## 🎯 Results")
    st.markdown(f"**🔢 Total vowels:** `{total_vowels}`")
    
    if total_vowels > 0:
        st.markdown("### 📊 Breakdown:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"🅰️ A: {vowel_counts['a']}")
        with col2:
            st.write(f"📧 E: {vowel_counts['e']}")
        with col3:
            st.write(f"📍 I: {vowel_counts['i']}")
        col4, col5 = st.columns(2)
        with col4:
            st.write(f"⭕ O: {vowel_counts['o']}")
        with col5:
            st.write(f"⛎ U: {vowel_counts['u']}")
    else:
        st.info("Hmm... no vowels found. Try a more *vocal* input!")

    # -------------------------------
    # Highlighted Input
    # -------------------------------
    st.markdown("### 🔦 Highlighted Input (Vowels in Red):")
    st.write(highlighted_text)

    # -------------------------------
    # Motivation Message
    # -------------------------------
    if total_vowels >= 10:
        st.success("🎉 That’s a vocal word! You’ve got rhythm in your sentence!")
    elif total_vowels >= 5:
        st.info("🟡 Decent vowel power — keep the words flowing!")
    else:
        st.warning("🟠 Just a few vowels — add some more sound!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ and Streamlit • #FlyHighwithAI 🔥")
