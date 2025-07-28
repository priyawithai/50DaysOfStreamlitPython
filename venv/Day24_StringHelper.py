# StringHelper.py

import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="🧠 String Helper Tool",
    page_icon="🦅",
    layout="centered"
)

# --- Header ---
st.title("🦅 String Helper Tool - Day 24")
st.markdown("Welcome to your mini string lab! 🔬\n\nThis tool helps you quickly **capitalize**, **reverse**, and **count** characters in any string. Perfect for learners, pros, and curious minds. #FlyHighwithAI 💡")

# --- User Input ---
user_input = st.text_area("✍️ Enter your text below:", height=150)

if user_input:
    # --- String Transformations ---
    capitalized = user_input.upper()
    reversed_text = user_input[::-1]
    count_with_spaces = len(user_input)
    count_without_spaces = len(user_input.replace(" ", ""))

    # --- Display Results ---
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔤 **Capitalized**")
        st.code(capitalized, language='text')
        st.caption("All letters converted to uppercase using `.upper()`.")

        st.markdown("🔢 **Character Count**")
        st.write(f"With spaces: `{count_with_spaces}` characters")
        st.write(f"Without spaces: `{count_without_spaces}` characters")

    with col2:
        st.markdown("🔁 **Reversed**")
        st.code(reversed_text, language='text')
        st.caption("String reversed using slicing `[::-1]`.")

    # --- Optional Features ---
    st.markdown("---")
    st.markdown("📥 **Export Results**")

    export_text = f"""
🔤 Capitalized:
{capitalized}

🔁 Reversed:
{reversed_text}

🔢 Character Count:
With spaces: {count_with_spaces}
Without spaces: {count_without_spaces}
"""
    st.download_button("📄 Download as TXT", export_text, file_name="string_results.txt")

else:
    st.info("👆 Enter some text above to begin your string transformation journey!")

# --- Footer ---
st.markdown("---")
st.caption("🦅 Day 24 – 50 Days of AI Python Challenge | Built with Streamlit 💡")
