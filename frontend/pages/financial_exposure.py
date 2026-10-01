import streamlit as st

st.set_page_config(
    page_title="Financial Exposure",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Financial Exposure")

st.write(
    "Estimate financial loss and calculate the return from security controls."
)

st.divider()

current_risk = st.number_input(
    "Current Risk Exposure (₹ Lakh)",
    min_value=0.0,
    value=12.0
)

expected_risk = st.number_input(
    "Expected Risk After Controls (₹ Lakh)",
    min_value=0.0,
    value=3.0
)

control_cost = st.number_input(
    "Security Control Cost (₹ Lakh)",
    min_value=0.0,
    value=2.0
)

if st.button("Calculate Financial Impact"):

    risk_reduction = current_risk - expected_risk

    if control_cost > 0:
        roi = (
            (risk_reduction - control_cost)
            / control_cost
        ) * 100
    else:
        roi = 0

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Current Risk",
            f"₹{current_risk:.2f} Lakh"
        )

    with col2:
        st.metric(
            "Expected Risk",
            f"₹{expected_risk:.2f} Lakh"
        )

    with col3:
        st.metric(
            "Risk Reduction",
            f"₹{risk_reduction:.2f} Lakh"
        )

    with col4:
        st.metric(
            "ROI",
            f"{roi:.2f}%"
        )

    st.success(
        f"Security investment can reduce risk by ₹{risk_reduction:.2f} Lakh."
    )