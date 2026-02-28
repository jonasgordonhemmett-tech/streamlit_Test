import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.html("""
<h1>Hello World</h1>
""")

userNum = st.text_input("Enter an integer: ")
if userNum:
    try:
        int(userNum)
        st.write(f"Your number is {userNum}")
    except:
        st.write("Please enter a valid number")