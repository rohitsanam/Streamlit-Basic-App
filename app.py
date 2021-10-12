import streamlit as st
st.title("Calculator")
st.write("Let us now take two numbers to perform basic arithmatic operations")
a = st.sidebar.number_input('Select the Value of a:')
b = st.sidebar.number_input('Select the Value of b:')

operations = ["Addition","Subtraction","Multiplication","Division"]
try:
    for operator in operations:
        if operator == "Addition":
            c = a+b
            st.write("The addition of three numbers are:",c)
    
        elif operator == "Subtraction":
            c = a-b
            st.write("The subtraction of two numbers are:",c)
    
        elif operator == "Multiplication":
            c = a*b
            st.write("The product of two numbers are:",c)
    
        elif operator == "Division":
            c = a/b
            st.write("The quotient after dividing two numbers is:",c)
except Exception as e:
    print("Type of exception handled is:",e)
    