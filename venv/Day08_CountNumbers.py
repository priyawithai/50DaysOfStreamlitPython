import streamlit as st
import matplotlib.pyplot as plt

# ---------------------- Page Config ---------------------- #
st.set_page_config(page_title="Count Numbers - Day 8", page_icon="🧮", layout="centered")

# ---------------------- Header Section ---------------------- #
st.markdown("""
    <h1 style='text-align: center; color: #6A0DAD;'>🦅 Day 8: Count Numbers</h1>
    <p style='text-align: center; font-size: 18px;'>Fly High with AI – Let's analyze your numbers with power and clarity! 🔥</p>
""", unsafe_allow_html=True)

# ---------------------- Input Section ---------------------- #
st.markdown("### 🎯 Enter numbers (comma-separated):")
user_input = st.text_input(
    "Enter numbers", 
    placeholder="-3.5, 0, 5, -1.2, 2.0, 0", 
    label_visibility="collapsed"
)

# ---------------------- Process Logic ---------------------- #
if user_input:
    try:
        numbers = [float(i.strip()) for i in user_input.split(",")]

        positive = sum(1 for i in numbers if i > 0)
        negative = sum(1 for i in numbers if i < 0)
        zero = sum(1 for i in numbers if i == 0)

        # ------------------ Results Section ------------------ #
        st.markdown("---")
        st.markdown("### 📊 Results Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success(f"✅ Positive: **{positive}**")
        with col2:
            st.error(f"❌ Negative: **{negative}**")
        with col3:
            st.info(f"0️⃣ Zero: **{zero}**")

        # ------------------ Chart Section ------------------ #
        st.markdown("### 📈 Distribution Chart")

        labels = ['Positive', 'Negative', 'Zero']
        counts = [positive, negative, zero]
        colors = ['#28a745', '#dc3545', '#17a2b8']

        fig, ax = plt.subplots()
        ax.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # ------------------ Motivational Insight ------------------ #
        max_count = max(counts)
        if max_count == positive:
            message = "🚀 You're radiating positivity! Keep going strong!"
        elif max_count == negative:
            message = "🔧 Challenges ahead? Flip the script and rise above!"
        else:
            message = "🌀 A balanced state — calm, neutral, and ready for takeoff!"

        st.markdown(f"### 🌟 Motivation Boost")
        st.markdown(f"<div style='font-size:18px; color:#4B0082;'>{message}</div>", unsafe_allow_html=True)

    except ValueError:
        st.warning("⚠️ Please enter only valid numbers separated by commas (e.g., `-2.7, 0, 5.1`).")

# ---------------------- Footer ---------------------- #
st.markdown("---")
st.markdown("""
    <div style='text-align: center; font-size: 16px;'>
        🧠 Powered by AI | 🚀 #FlyHighwithAI | 🔥 Day 8 Complete
    </div>
""", unsafe_allow_html=True)
