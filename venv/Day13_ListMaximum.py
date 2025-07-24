import streamlit as st

st.set_page_config(page_title="List Maximum Finder 🏆", page_icon="🦅", layout="centered")

st.title("🦅 Day 13 – List Maximum Finder")
st.subheader("Find the Largest Number Without Using `max()` 💡")
st.markdown("Enter a list of numbers separated by commas (e.g., `5, 3, 9, 1, 10`) and let’s find the **🏆 biggest one manually!**")

# Input Section
user_input = st.text_input("🔢 Enter numbers (comma-separated):", "")

if user_input:
    try:
        # Convert input into a list of integers
        number_list = [int(num.strip()) for num in user_input.split(',')]

        # Manual maximum logic
        largest = number_list[0]
        steps = [f"Start with first number: **{largest}**"]

        for i in range(1, len(number_list)):
            current = number_list[i]
            steps.append(f"Compare with **{current}** → {'✅ Update!' if current > largest else '❌ Keep current max'}")
            if current > largest:
                largest = current

        # Display results
        st.markdown("---")
        st.markdown("### 🔍 Step-by-Step Comparison")
        for step in steps:
            st.markdown(f"- {step}")

        st.markdown("---")
        st.success(f"🏆 The largest number is: **{largest}**")
        st.balloons()

    except ValueError:
        st.error("⚠️ Please enter a valid list of integers, separated by commas.")
else:
    st.info("👆 Awaiting input to begin...")

st.markdown("---")
st.caption("Made with ❤️ for the 50-Day AI Python Challenge — #FlyHighwithAI 🔥")
