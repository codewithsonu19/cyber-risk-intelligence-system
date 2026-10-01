import streamlit as st


def show_risk_chart():
    risk_data = {
        "Critical": 5,
        "High": 8,
        "Medium": 7,
        "Low": 5
    }

    st.bar_chart(risk_data)