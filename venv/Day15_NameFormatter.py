import streamlit as st
import re

# 🎉 App Title and Introduction
st.set_page_config(page_title="Name Formatter", page_icon="📝")
st.title("📝 Name Formatter")
st.subheader("Format your full name in multiple creative ways ✨")
st.markdown("Welcome to **Day 15** of the **AI Python Challenge** 🦅 — Let’s polish up your name formats with #FlyHighwithAI 🚀")

# 🧾 Input Section
full_name = st.text_input("✍️ Enter your full name (First Last):", "")

def clean_name(name):
    # Remove extra spaces and non-alpha characters
    cleaned = re.sub(r"[^a-zA-Z\s]", "", name).strip()
    parts = cleaned.split()
    return parts if len(parts) == 2 else None

if full_name:
    name_parts = clean_name(full_name)

    if name_parts:
        first, last = name_parts

        # 🧠 Formatting Variations
        formatted_outputs = {
            "🔁 Last, First": f"{last}, {first}",
            "👫 First Last": f"{first} {last}",
            "🆎 Initials": f"{first[0].upper()}.{last[0].upper()}.",
            "🔠 UPPERCASE": full_name.upper(),
            "🔡 lowercase": full_name.lower(),
            "📚 Title Case": full_name.title()
        }

        st.success("✅ Name successfully formatted! See the variations below:")

        # 💡 Display each format
        for label, output in formatted_outputs.items():
            st.code(f"{label}: {output}", language="text")

        # 📥 Optional: Download as Text File
        output_text = "\n".join([f"{label}: {val}" for label, val in formatted_outputs.items()])
        st.download_button("📥 Download Formats", output_text, file_name="name_formats.txt")

    else:
        st.warning("⚠️ Please enter a valid full name with **First** and **Last** only (e.g., John Doe).")

# 👣 Footer
st.markdown("---")
st.caption("Built with ❤️ by AI on Day 15 of the #FlyHighwithAI Challenge 🦅")
