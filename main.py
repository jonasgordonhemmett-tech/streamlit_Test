import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



st.html("""
<h1>Hello World</h1>
""")

def isPrime(n, divisor=2):
    if n < 2:
        return False
    if divisor ** 2 > n:
        return True
    if n % divisor == 0:
        return False
    return isPrime(n, divisor+1)

userNum = st.text_input("Enter an integer: ")

if userNum:
    try:
        userNum = int(userNum)
        st.write(f"Your integer is {userNum}")
        st.write(f"{userNum} is {"prime" if isPrime(userNum) else "not prime"}.")


    except:
        st.write("Please enter a valid integer number")
    
