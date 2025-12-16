import streamlit as st
import math

st.header("Scientific Functions")

operation = st.selectbox(
    "Choose operation",
    ["Square Root", "Power", "Sin", "Cos", "Tan", "Log"]
)

value = st.number_input("Enter value", value=0.0, step=0.1)

# Show power input only when needed
power = 2.0
if operation == "Power":
    power = st.number_input("Enter power", value=2.0, step=0.1)

if st.button("Calculate"):
    # Reset any previous messages
    # (optional but nice – clears old success/error when clicking again)
    # st.empty() or just let new messages overwrite

    if operation == "Square Root":
        if value < 0:
            st.error("Cannot calculate square root of a negative number!")
        else:
            result = math.sqrt(value)
            st.success(f"√{value} = {result:.6f}")

    elif operation == "Power":
        result = math.pow(value, power)
        st.success(f"{value} ^ {power} = {result:.6f}")

    elif operation == "Sin":
        result = math.sin(math.radians(value))
        st.success(f"sin({value}°) = {result:.6f}")

    elif operation == "Cos":
        result = math.cos(math.radians(value))
        st.success(f"cos({value}°) = {result:.6f}")

    elif operation == "Tan":
        result = math.tan(math.radians(value))
        st.success(f"tan({value}°) = {result:.6f}")

    elif operation == "Log":
        if value <= 0:
            st.error("Log is only defined for positive numbers (> 0)!")
        else:
            result = math.log(value)        # natural log
            st.success(f"ln({value}) = {result:.6f}")
