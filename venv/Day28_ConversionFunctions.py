# ConversionFunctions.py

import streamlit as st

# Set the page config
st.set_page_config(page_title="Unit Converter - Day 28", page_icon="🧮", layout="centered")

# App title
st.title("📐 Unit Converter")
st.subheader("Welcome to Day 28 of the AI Python Challenge 🦅")
st.markdown("Convert between common units easily and instantly! #FlyHighwithAI 💡")

# Conversion functions
def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

# Select conversion category
conversion_type = st.selectbox(
    "Select a conversion type:",
    (
        "📏 Feet ➡️ Meters",
        "📏 Meters ➡️ Feet",
        "⚖️ Pounds ➡️ Kilograms",
        "⚖️ Kilograms ➡️ Pounds"
    )
)

# Input and output section
st.markdown("---")

if conversion_type == "📏 Feet ➡️ Meters":
    feet = st.number_input("Enter value in feet:", min_value=0.0, step=0.1)
    meters = feet_to_meters(feet)
    st.success(f"✅ {feet} feet = {meters:.4f} meters")
    st.caption("📏 Formula: 1 ft = 0.3048 m")

elif conversion_type == "📏 Meters ➡️ Feet":
    meters = st.number_input("Enter value in meters:", min_value=0.0, step=0.1)
    feet = meters_to_feet(meters)
    st.success(f"✅ {meters} meters = {feet:.4f} feet")
    st.caption("📏 Formula: 1 m = 3.2808 ft")

elif conversion_type == "⚖️ Pounds ➡️ Kilograms":
    pounds = st.number_input("Enter weight in pounds:", min_value=0.0, step=0.1)
    kg = pounds_to_kg(pounds)
    st.success(f"✅ {pounds} lbs = {kg:.4f} kg")
    st.caption("⚖️ Formula: 1 lb = 0.453592 kg")

elif conversion_type == "⚖️ Kilograms ➡️ Pounds":
    kg = st.number_input("Enter weight in kilograms:", min_value=0.0, step=0.1)
    pounds = kg_to_pounds(kg)
    st.success(f"✅ {kg} kg = {pounds:.4f} lbs")
    st.caption("⚖️ Formula: 1 kg = 2.2046 lbs")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ for the **AI Python Challenge - Day 28** 🦅")
st.markdown("**#FlyHighwithAI 💡** | Precision in every pixel.")
