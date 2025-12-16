import streamlit as st
import math
# Title
st.title("Basic Web Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide","Square Root", "Power", "Sin", "Cos", "Tan"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Power":
        result = math.pow(num1, num2)
    elif operation == "Sin":
        result = math.sin(math.radians(num1))
    elif operation == "Cos":
        result = math.cos(math.radians(num1))
    elif operation == "Tan":
        result = math.tan(math.radians(num1))
    

    st.success(f"Result: {result}")
