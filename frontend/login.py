import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CyRIQ Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Login check
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    if st.button("Go to Login"):
        st.switch_page("dashboard.py")
    st.stop()

# CSS
css_file = Path(__file__).parent.parent / "styles" / "style.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🛡️ CyRIQ")
st.subheader("AI-Powered Continuous Cyber Risk Quantification Platform")

st.write(
    "Monitor cyber risk, financial exposure and security investments."
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Assets", "25")

with col2:
    st.metric("Critical Risks", "5")

with col3:
    st.metric("Risk Exposure", "₹42 Lakh")

with col4:
    st.metric("Potential Savings", "₹18 Lakh")

st.divider()

st.header("Risk Overview")

risk_data = {
    "Critical": 5,
    "High": 8,
    "Medium": 7,
    "Low": 5
}

st.bar_chart(risk_data)

st.header("Top Risky Assets")

assets = [
    ["Customer Database", "Database", 9.8, "Critical"],
    ["Payment Server", "Server", 9.5, "Critical"],
    ["Employee Portal", "Web Application", 7.8, "High"],
    ["Email Server", "Server", 6.5, "High"],
]

st.table(
    {
        "Asset": [x[0] for x in assets],
        "Type": [x[1] for x in assets],
        "CVSS": [x[2] for x in assets],
        "Priority": [x[3] for x in assets],
    }
)