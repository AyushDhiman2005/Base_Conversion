import streamlit as st
import pandas as pd
import new_project as method
import get_code as gc


st.title("Quad Radix")
st.divider()

col1 , col2 = st.columns(2)

number=''
radio1=''
radio2=''
initial_base=2
final_base=2



with col1:
    radio1 = st.radio(
        "From",
        ('Binary','Octal','Decimal','Hexadecimal')
    )
    initial_base=gc.getCode(radio1)
    st.write(initial_base)
    st.write("\n\n\n")
    number=st.text_input(f"Enter {radio1} Number: ")
    
with col2:
    radio2=st.radio(
        "To",
        ('Binary','Octal','Decimal','Hexadecimal')
    )
    final_base = gc.getCode(radio2)
    st.write(final_base)



st.write(f"Converting {number}({initial_base}) into {radio2}")



  
result = method.any_to_any(number,initial_base,final_base)
st.write(f"Result: {result}")
