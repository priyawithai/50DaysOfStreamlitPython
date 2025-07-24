import streamlit as st
import time

# --- App Branding ---
st.set_page_config(page_title="🛒 Smart AI Checkout - Day 5", layout="centered")

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: #6A0DAD;'>🛍️ AI-Powered Shopping Bill Calculator</h1>
    <p style='text-align: center; font-size: 18px;'>Welcome to Day 5 of the <b>#FlyHighwithAI ✨</b> Challenge</p>
    <p style='text-align: center;'>Let's create your smart, seamless shopping checkout experience!</p>
""", unsafe_allow_html=True)

# --- Input Fields for Items ---
st.header("🧾 Enter Item Details")
col1, col2 = st.columns(2)

with col1:
    item1_name = st.text_input("Item 1 Name", value="Apple")
    item2_name = st.text_input("Item 2 Name", value="Milk")
    item3_name = st.text_input("Item 3 Name", value="Bread")

with col2:
    item1_price = st.number_input("Item 1 Price (₹)", min_value=0.0, format="%.2f")
    item2_price = st.number_input("Item 2 Price (₹)", min_value=0.0, format="%.2f")
    item3_price = st.number_input("Item 3 Price (₹)", min_value=0.0, format="%.2f")

# --- Tax and Discount Section ---
st.header("📊 Tax & Discount")
tax_percent = st.slider("Select Tax Percentage (%)", 0, 30, 5)
discount_code = st.text_input("Optional: Enter Discount Code (try 'EAGLE10')")

# --- Calculate Button ---
if st.button("🧮 Calculate Total"):
    with st.spinner("Calculating your smart bill..."):
        time.sleep(1)

        # --- Computation Logic ---
        subtotal = item1_price + item2_price + item3_price
        tax_amount = (tax_percent / 100) * subtotal

        discount = 0
        if discount_code.upper() == "EAGLE10":
            discount = 0.1 * subtotal

        total = subtotal + tax_amount - discount

        st.success("✅ Bill generated successfully!")
        st.balloons()

        # --- Output Receipt ---
        st.markdown("---")
        st.markdown("### 🧾 Your AI Receipt:")
        st.markdown(f"""
        <div style='background-color:#f0f0f5;padding:15px;border-radius:10px;color:#222222;font-size:16px;'>
            <b>Items Purchased:</b><br>
            • {item1_name}: ₹{item1_price:.2f}<br>
            • {item2_name}: ₹{item2_price:.2f}<br>
            • {item3_name}: ₹{item3_price:.2f}<br><br>
            <b>Subtotal:</b> ₹{subtotal:.2f}<br>
            <b>Tax ({tax_percent}%):</b> ₹{tax_amount:.2f}<br>
            <b>Discount:</b> -₹{discount:.2f}<br><hr>
            <h4 style='color:#4CAF50;'>Grand Total: ₹{total:.2f}</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.info("Thank you for shopping smartly with AI! 🛍️✨ #FlyHighwithAI")
