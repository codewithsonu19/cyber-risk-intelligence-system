import streamlit as st


def show_metrics(
    total_assets,
    critical_risks,
    risk_exposure,
    potential_savings
):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Assets", total_assets)

    with col2:
        st.metric("Critical Risks", critical_risks)

    with col3:
        st.metric("Risk Exposure", risk_exposure)

    with col4:
        st.metric("Potential Savings", potential_savings)