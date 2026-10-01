import streamlit as st

st.set_page_config(
    page_title="Risk Quantification",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Risk Quantification")

st.write(
    "Calculate the financial exposure caused by cyber risks."
)

st.divider()

criticality = st.number_input(
    "Asset Criticality",
    min_value=0.0,
    max_value=10.0,
    value=9.0
)

cvss = st.number_input(
    "CVSS Score",
    min_value=0.0,
    max_value=10.0,
    value=9.8
)

likelihood = st.number_input(
    "Likelihood",
    min_value=0.0,
    max_value=1.0,
    value=0.6
)

estimated_loss = st.number_input(
    "Estimated Loss (₹ Lakh)",
    min_value=0.0,
    value=20.0
)

if st.button("Calculate Risk"):

    risk_exposure = estimated_loss * likelihood

    risk_score = (
        criticality * 0.4
        + cvss * 0.4
        + likelihood * 10 * 0.2
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Exposure",
            f"₹{risk_exposure:.2f} Lakh"
        )

    with col2:
        st.metric(
            "Risk Score",
            f"{risk_score:.2f} / 10"
        )

    if risk_score >= 8:
        st.error("Risk Level: Critical")
    elif risk_score >= 6:
        st.warning("Risk Level: High")
    elif risk_score >= 4:
        st.info("Risk Level: Medium")
    else:
        st.success("Risk Level: Low")