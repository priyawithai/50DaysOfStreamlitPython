import streamlit as st
import matplotlib.pyplot as plt

# App Title
st.set_page_config(page_title="List Helper Tool 🧠", page_icon="📊")
st.title("📊 List Helper Tool")
st.subheader("Analyze your numbers with smart insights ✨")
st.markdown("Welcome to **Day 26** of the #FlyHighwithAI Challenge 🦅 — let's explore your list with style and logic!")

# --- Helper Functions ---
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_min(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_average(numbers):
    return find_sum(numbers) / len(numbers)

# --- Input Section ---
user_input = st.text_input("Enter numbers separated by commas (e.g., 5, 10, -2, 8)", "")

if user_input:
    try:
        number_list = [float(i.strip()) for i in user_input.split(",")]
        st.success("✅ Input processed successfully!")

        # Compute results
        max_val = find_max(number_list)
        min_val = find_min(number_list)
        total = find_sum(number_list)
        avg = find_average(number_list)

        # --- Display Section ---
        st.markdown("### 📈 Results Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"🔼 **Maximum**: {max_val}")
            st.info(f"🔽 **Minimum**: {min_val}")
        with col2:
            st.success(f"➕ **Sum**: {total}")
            st.warning(f"📊 **Average**: {avg:.2f}")

        # --- Optional Bonus: Chart ---
        st.markdown("### 📉 Bar Chart of Values")
        fig, ax = plt.subplots()
        ax.bar(range(len(number_list)), number_list, color="skyblue")
        ax.set_title("Your Numbers")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        st.pyplot(fig)

    except ValueError:
        st.error("❌ Please enter only numbers separated by commas.")
else:
    st.info("💡 Tip: Try input like `5, 10, -2, 8` to get started!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ for the **AI Python Challenge** • #FlyHighwithAI 🦅")
