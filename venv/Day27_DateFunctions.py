import streamlit as st
from datetime import datetime, date

# App Configuration
st.set_page_config(page_title="Date Functions - AI Python Challenge", page_icon="🗓️")

st.title("🗓️ Date Functions App")
st.subheader("Welcome to Day 27 of the AI Python Challenge! 🦅")
st.markdown("Explore **Leap Year Check** and **Age Calculator** with a smart and friendly UI 💡")

st.divider()

# 🔁 Leap Year Checker
st.header("🔁 Leap Year Checker")
year = st.number_input("Enter a year to check if it's a leap year:", min_value=0, max_value=9999, step=1)

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if year:
    if is_leap_year(year):
        st.success(f"✅ Yes, {year} is a Leap Year!")
    else:
        st.error(f"❌ No, {year} is not a Leap Year.")
    st.caption("📘 A leap year occurs every 4 years, except for years that are divisible by 100 but not 400.")

st.divider()

# 👶 Age Calculator
st.header("👶 Age Calculator")

dob = st.date_input(
    "Select your Date of Birth:",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

def calculate_age(dob):
    today = date.today()
    age_days = (today - dob).days
    age_years = age_days / 365.25  # Including leap years
    return round(age_years, 2)

if dob:
    age = calculate_age(dob)
    st.info(f"🎂 You are **{age} years** old.")
    
    weekday_born = dob.strftime("%A")
    st.write(f"🗓️ You were born on a **{weekday_born}**.")

    # 🎉 Fun Extras
    if dob.month == 2 and dob.day == 29:
        st.warning("🤯 You were born on a Leap Day! So special!")
    
    current_year = datetime.now().year
    turning_age = current_year - dob.year
    if turning_age == 30:
        st.success("🎉 You're turning 30 this year – milestone alert!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | #FlyHighwithAI 🦅")
