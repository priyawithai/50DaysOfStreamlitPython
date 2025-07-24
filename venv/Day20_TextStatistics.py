import streamlit as st
import matplotlib.pyplot as plt
import re
from collections import Counter

# -----------------------
# Streamlit App UI
# -----------------------
st.set_page_config(page_title="Text Statistics", page_icon="📊", layout="wide")
st.title("📊 Text Statistics Analyzer")
st.markdown("Welcome to your **mini NLP dashboard**! Paste a paragraph below to see an instant breakdown of your text. Let’s #FlyHighwithAI 🦅")

# -----------------------
# Text Input
# -----------------------
text_input = st.text_area("✍️ Enter your paragraph below:", height=200)

# -----------------------
# Text Analysis Function (No NLTK)
# -----------------------
def analyze_text(text):
    # Basic regex-based tokenization
    sentences = re.split(r'[.!?]+', text.strip())
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', text)
    char_with_spaces = len(text)
    char_without_spaces = len(text.replace(" ", ""))
    reading_time = round(len(words) / 200, 2)  # Avg reading speed: 200 wpm
    freq = Counter([word.lower() for word in words])
    most_common_word = freq.most_common(1)[0] if freq else ("None", 0)

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "char_with_spaces": char_with_spaces,
        "char_without_spaces": char_without_spaces,
        "reading_time": reading_time,
        "most_common_word": most_common_word
    }

# -----------------------
# Display Stats
# -----------------------
if text_input.strip():
    stats = analyze_text(text_input)

    # Stats Summary Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📝 Words", stats['word_count'])
    col2.metric("📖 Sentences", stats['sentence_count'])
    col3.metric("🔡 Chars (with spaces)", stats['char_with_spaces'])
    col4.metric("🔠 Chars (no spaces)", stats['char_without_spaces'])

    st.markdown("----")
    
    # Bonus Info
    col5, col6 = st.columns(2)
    col5.success(f"⏱️ Estimated Reading Time: **{stats['reading_time']} min**")
    col6.info(f"🔍 Most Frequent Word: **'{stats['most_common_word'][0]}'** ({stats['most_common_word'][1]} times)")

    # Emoji reaction
    if stats['word_count'] < 50:
        st.warning("🧠 Short and snappy!")
    elif stats['word_count'] < 150:
        st.info("💬 Nice chunk of content!")
    else:
        st.success("📚 That’s a detailed write-up!")

    # -----------------------
    # Chart Visualization
    # -----------------------
    st.markdown("### 📊 Visual Summary")
    labels = ['Words', 'Sentences', 'Chars (w/ spaces)', 'Chars (no spaces)']
    values = [stats['word_count'], stats['sentence_count'], stats['char_with_spaces'], stats['char_without_spaces']]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['skyblue', 'lightgreen', 'orange', 'salmon'])
    plt.xticks(rotation=15)
    st.pyplot(fig)

    st.markdown("----")
    st.markdown("""
    🧩 **How this works:**  
    - **Words**: Counted using regex word matching  
    - **Sentences**: Split using punctuation (.!?)
    - **Characters**: Raw length with/without spaces  
    - **Reading Time**: Estimated at 200 words per minute  
    - **Most Frequent Word**: Based on simple frequency (case-insensitive)  
    """)
else:
    st.info("Awaiting your paragraph to begin analysis... 🚀")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Crafted with 💻 and ☕ on Day 20 of the #AI Python Challenge | #FlyHighwithAI 🦅")
