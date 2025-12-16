import streamlit as st
# Title
st.title("Basic Web Calculator")
# Input fields
num1 = st.number_input("Enter the first number", value = 0.0)
num2 = st.number_input("Enter the second number", value = 0.0)
# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"] 
# Calculate
if st.button("Calculation"):
  if operation == "Add":
      result = num1 + num2
  elif operation == "Subtract":
      result = num1 - num2
  elif operation == "Multiply":
      result == num1 * numb2
  elif operateion == "Divide":
      result = num1 / num2 if num2 != 0 else "Error: Divsion by zero"
st.success(f"Result:{result}")
