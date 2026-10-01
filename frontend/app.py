import streamlit as st

st.set_page_config(
    page_title="CyRIQ Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 CyRIQ")
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.session_state["logged_in"] = True
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid username or password")
        st.write("Don't have an account?")

if st.button("Register"):
    st.switch_page("pages/register.py")
