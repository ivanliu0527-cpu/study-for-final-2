import math
import streamlit as st
st.header("Scientific Functions")
operation_sci = st.selectbox("Choose scientific operation", ["Square Root", "Power", "Sin", "Cos", "Tan","Log"])

value = st.number_input("Enter value", value=0.0)
power = st.number_input("Enter power (if applicable)", value=0.0)

if st.button("Calculate Scientific"):
    if operation_sci == "Square Root":
      if value < 0:
                st.error("Cannot calculate square root of a negative number!")
      else:
                result = math.sqrt(value)
    elif operation_sci == "Power":
        result = math.pow(value, power)
    elif operation_sci == "Sin":
        result = math.sin(math.radians(value))
    elif operation_sci == "Cos":
        result = math.cos(math.radians(value))
    elif operation_sci == "Tan":
        result = math.tan(math.radians(value))
    elif operation_sci == "Log":
      if value <= 0:
                st.error("Natural log is only defined for positive numbers!")
      else:
                result = math.log(value)

    st.success(f"Result: {result}") if no error 
