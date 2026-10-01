import streamlit as st

st.set_page_config(
    page_title="CyRIQ Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Account")
st.subheader("Register for CyRIQ")

name = st.text_input("Full Name")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Register button
if st.button("Register", use_container_width=True):
    if not name or not username or not password or not confirm_password:
        st.error("Please fill all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        st.session_state["registered_name"] = name
        st.session_state["registered_username"] = username
        st.session_state["registered_password"] = password

        st.success("Registration successful! 🎉")
        st.info("You can now go to the login page.")

# Login button
if st.button("Already have an account? Login", use_container_width=True):
    st.switch_page("app.py")
