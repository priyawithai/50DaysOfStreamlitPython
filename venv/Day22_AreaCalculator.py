import streamlit as st
import math

# --- Page Config ---
st.set_page_config(page_title="Area Calculator 🧮", page_icon="📐")

# --- Title ---
st.title("📐 Area Calculator - Geometry Toolkit")
st.markdown("Welcome to **Day 22** of the **AI Python Challenge** 🦅")
st.write("Let’s explore area formulas interactively with the power of **Streamlit**! 💡")

# --- Shape Selection ---
shape = st.selectbox(
    "Choose a shape to calculate area:",
    ("🟠 Circle", "🟥 Rectangle", "🔺 Triangle")
)

# --- Functions to Calculate Area ---
def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(width, height):
    return width * height

def calculate_triangle_area(base, height):
    return 0.5 * base * height

# --- Input and Logic ---
if "Circle" in shape:
    st.subheader("🟠 Circle Area")
    radius = st.number_input("Enter radius (r)", min_value=0.0, format="%.2f")
    if radius > 0:
        area = calculate_circle_area(radius)
        st.markdown(f"**Formula:** π × r²**  →  π × {radius}²**")
        st.success(f"Area: {area:.2f} square units")

elif "Rectangle" in shape:
    st.subheader("🟥 Rectangle Area")
    width = st.number_input("Enter width (w)", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height (h)", min_value=0.0, format="%.2f")
    if width > 0 and height > 0:
        area = calculate_rectangle_area(width, height)
        st.markdown(f"**Formula:** w × h  →  {width} × {height}")
        st.success(f"Area: {area:.2f} square units")

elif "Triangle" in shape:
    st.subheader("🔺 Triangle Area")
    base = st.number_input("Enter base (b)", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height (h)", min_value=0.0, format="%.2f")
    if base > 0 and height > 0:
        area = calculate_triangle_area(base, height)
        st.markdown(f"**Formula:** (1/2) × b × h  →  0.5 × {base} × {height}")
        st.success(f"Area: {area:.2f} square units")

# --- Footer ---
st.markdown("---")
st.markdown("🦅 Built with Streamlit on **Day 22** of the #FlyHighwithAI challenge!")
