import streamlit as st
import pyperclip

# App title
st.set_page_config(page_title="Word Reverser 🪞", page_icon="🔄", layout="centered")
st.title("🔄 Word Reverser Playground 🧠")
st.caption("Reverse each word individually — and see the magic! ✨ #FlyHighwithAI 🚀")

# Input section
sentence = st.text_input("Enter a sentence to reverse each word:", placeholder="e.g. Hello Eagles, keep flying high!")

# Reversal logic
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())

# Display section
if sentence:
    reversed_sentence = reverse_words(sentence)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔹 Original Sentence")
        st.code(sentence, language="text")

    with col2:
        st.subheader("🔹 Reversed Words")
        st.code(reversed_sentence, language="text")

    # Copy button
    if st.button("📋 Copy Result"):
        pyperclip.copy(reversed_sentence)
        st.success("Reversed sentence copied to clipboard! ✅")

    # Bonus stats
    st.markdown("---")
    st.markdown("📊 **Quick Stats**")
    st.markdown(f"- 🔤 **Word Count:** `{len(sentence.split())}`")
    st.markdown(f"- 💬 **Vowel Count:** `{sum(1 for c in sentence.lower() if c in 'aeiou')}`")

else:
    st.info("Enter a sentence above and watch each word flip like magic! 🪄")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by the AI Python Challenge team — Day 16/50 🦅")
