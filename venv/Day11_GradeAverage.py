import streamlit as st
import numpy as np

# 🦅 Title and Subheader
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🦅 Day 11: Grade Average Analyzer</h1>
    <p style='text-align: center; font-size: 18px;'>Welcome to the #FlyHighwithAI Challenge – Let’s check those grades and aim high! 🎯</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 🎯 Input Scores
st.subheader("🔢 Enter Your Test Scores (0 - 100)")

scores = []
for i in range(1, 6):
    score = st.slider(f"Test Score {i}", min_value=0, max_value=100, value=50, step=1)
    scores.append(score)

# ✏️ Optional Threshold
threshold = st.slider("📊 Set Pass Threshold", min_value=0, max_value=100, value=50, step=1)

# 🧠 Calculate Average
average = np.mean(scores)

# 🎨 Display Result
st.markdown("## 🎓 Result")
st.progress(int(average))

if average >= threshold:
    st.success(f"✅ You Passed! Average Score: {average:.2f}%")
    st.markdown("### 🌟 Great job! Keep soaring high, Eagle! 🦅")
    st.markdown("#### 🟢 Confidence Level: High")
else:
    st.error(f"❌ You Failed. Average Score: {average:.2f}%")
    st.markdown("### 🛠️ Keep going! Every fail is a step to success.")
    st.markdown("#### 🔴 Confidence Level: Low")

# 📊 Bonus: Emoji Feedback
st.markdown("## 💬 Feedback Emoji")
if average >= 90:
    st.markdown("🥇 Excellent! You're flying high!")
elif average >= 75:
    st.markdown("👏 Good job! Keep climbing!")
elif average >= 50:
    st.markdown("😊 Not bad! There's room to improve.")
else:
    st.markdown("💡 Let’s study harder next time!")

# 🪄 Footer
st.markdown("---")
st.markdown("<center>🚀 Built with 💙 by AI • Day 11 • #FlyHighwithAI 🔥</center>", unsafe_allow_html=True)
