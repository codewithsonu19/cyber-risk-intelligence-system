import streamlit as st

st.set_page_config(
    page_title="Investment Optimization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Investment Optimization")

st.write(
    "Find security investments that provide better risk reduction."
)

st.divider()

budget = st.number_input(
    "Available Security Budget (₹ Lakh)",
    min_value=0.0,
    value=10.0
)

control_cost = st.number_input(
    "Control Cost (₹ Lakh)",
    min_value=0.0,
    value=2.0
)

risk_reduction = st.number_input(
    "Expected Risk Reduction (₹ Lakh)",
    min_value=0.0,
    value=9.0
)

if st.button("Optimize Investment"):

    if control_cost <= budget and control_cost > 0:

        roi = (
            (risk_reduction - control_cost)
            / control_cost
        ) * 100

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Investment",
                f"₹{control_cost:.2f} Lakh"
            )

        with col2:
            st.metric(
                "Risk Reduction",
                f"₹{risk_reduction:.2f} Lakh"
            )

        with col3:
            st.metric(
                "ROI",
                f"{roi:.2f}%"
            )

        st.success(
            "Recommended: This security investment fits the available budget."
        )

    elif control_cost > budget:

        st.error(
            "Budget is insufficient for this security control."
        )

    else:

        st.warning(
            "Please enter a valid control cost."
        )