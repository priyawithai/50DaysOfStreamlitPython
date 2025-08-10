# NumberFileProcessor.py
import streamlit as st

# --- App Config ---
st.set_page_config(page_title="Number File Processor 📊", page_icon="📁", layout="centered")
st.title("📊 Number File Processor")
st.subheader("Day 30 — Halfway Mark! 🦅 #FlyHighwithAI")

st.markdown("""
Upload a `.txt` or `.csv` file containing numbers (one per line or comma-separated)  
and instantly get **sum**, **average**, and more 📈.
""")

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Choose a file", type=["txt", "csv"])

if uploaded_file is not None:
    try:
        # Read file content
        content = uploaded_file.read().decode("utf-8")
        
        # Detect and split by newlines or commas
        raw_numbers = []
        for line in content.splitlines():
            parts = line.replace(",", " ").split()
            raw_numbers.extend(parts)
        
        # Convert to floats where possible
        numbers = []
        skipped = []
        for item in raw_numbers:
            try:
                numbers.append(float(item))
            except ValueError:
                skipped.append(item)
        
        if numbers:
            total_sum = sum(numbers)
            average = total_sum / len(numbers)
            min_val = min(numbers)
            max_val = max(numbers)
            count = len(numbers)

            # 🎯 Display results
            col1, col2, col3 = st.columns(3)
            col1.metric("🔢 Count", count)
            col2.metric("➕ Sum", f"{total_sum:.2f}")
            col3.metric("📊 Average", f"{average:.2f}")

            col4, col5 = st.columns(2)
            col4.metric("📉 Min", f"{min_val:.2f}")
            col5.metric("📈 Max", f"{max_val:.2f}")

            # Show numbers list
            with st.expander("📜 View Numbers List"):
                st.write(numbers)

            # Warn if any skipped values
            if skipped:
                st.warning(f"⚠️ Skipped {len(skipped)} non-numeric entries: {', '.join(skipped[:5])}{'...' if len(skipped) > 5 else ''}")
        else:
            st.error("❌ No valid numeric data found in the file.")

    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")
else:
    st.info("⬆️ Upload a `.txt` or `.csv` file to begin processing.")
