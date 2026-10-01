import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="CyRIQ Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# User must be logged in to open the dashboard
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")

    if st.button("Go to Login"):
        st.switch_page("app.py")

    st.stop()


user_name = st.session_state.get(
    "registered_name",
    st.session_state.get("current_user", "Admin"),
)


# Sidebar
with st.sidebar:
    st.title("🛡️ CyRIQ")
    st.caption("Cyber Risk Intelligence")

    st.divider()
    st.caption("WORKSPACE")

    if st.button("📊 Dashboard", use_container_width=True):
        st.rerun()

    if st.button("🖥️ Assets", use_container_width=True):
        st.switch_page("pages/assets.py")

    if st.button("⚠️ Risk Assessment", use_container_width=True):
        st.switch_page("pages/risks.py")

    if st.button("💰 Financial Impact", use_container_width=True):
        st.switch_page("pages/financial.py")

    if st.button("🔐 Security Controls", use_container_width=True):
        st.switch_page("pages/security.py")

    if st.button("📄 Reports", use_container_width=True):
        st.switch_page("pages/reports.py")

    st.divider()
    st.caption("ACCOUNT")

    if st.button("⚙️ Settings", use_container_width=True):
        st.switch_page("pages/settings.py")

    if st.button("🚪 Sign out", use_container_width=True):
        st.session_state["logged_in"] = False
        st.switch_page("app.py")


st.title(f"Good morning, {user_name} 👋")
st.write("Here is a quick overview of your organization's security posture.")

st.divider()


# Main numbers
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🖥️ Total Assets", "25", "+3 this month")

with col2:
    st.metric("🔴 Critical Risks", "5", "-2 this week")

with col3:
    st.metric("💰 Estimated Exposure", "₹42 Lakh", "-8% from last month")

with col4:
    st.metric("🛡️ Security Score", "78 / 100", "+6 points")


st.write("")


# Risk chart and security score
left, right = st.columns([1.5, 1])

with left:
    st.subheader("Risk overview")
    st.caption("Current distribution of identified security risks.")

    risk_data = pd.DataFrame({
        "Priority": ["Critical", "High", "Medium", "Low"],
        "Count": [5, 8, 7, 5],
    })

    fig = px.bar(
        risk_data,
        x="Priority",
        y="Count",
        color="Priority",
        color_discrete_map={
            "Critical": "#dc2626",
            "High": "#f59e0b",
            "Medium": "#eab308",
            "Low": "#22c55e",
        },
    )

    fig.update_traces(texttemplate="%{y}", textposition="outside")
    fig.update_layout(
        height=350,
        showlegend=False,
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis_title=None,
        yaxis_title="Number of Risks",
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, rangemode="tozero")

    st.plotly_chart(fig, use_container_width=True)


with right:
    st.subheader("Security health")
    st.metric("Overall Security Score", "78 / 100", "+6 points")
    st.progress(0.78)
    st.caption(
        "Your security posture is good, but some high-impact risks require attention."
    )


st.divider()


# Things that need attention
risk_col, activity_col = st.columns([1.2, 1])

with risk_col:
    st.subheader("⚠️ Needs your attention")

    st.error("🔴 Payment Server — Critical vulnerability detected.  CVSS 9.5")
    st.error("🔴 Customer Database — Database exposure requires immediate review.  CVSS 9.8")
    st.warning("🟠 Employee Portal — Security configuration should be reviewed.  CVSS 7.8")


with activity_col:
    st.subheader("🕒 Recent activity")

    st.success("🟢 Vulnerability scan completed — All 25 assets scanned · 20 minutes ago")
    st.info("🔵 Payment Server updated — Risk score changed to 9.5 · 1 hour ago")
    st.warning("🟡 Security review required — 3 controls need attention · 2 hours ago")
    st.success("🟢 Backup verification completed — Backup integrity check passed · 4 hours ago")


st.divider()


# Top risky assets
st.subheader("🖥️ Top risky assets")
st.caption("Assets with the highest current vulnerability scores.")

assets = pd.DataFrame([
    {
        "Asset": "Customer Database",
        "Type": "Database",
        "CVSS": 9.8,
        "Priority": "Critical",
    },
    {
        "Asset": "Payment Server",
        "Type": "Server",
        "CVSS": 9.5,
        "Priority": "Critical",
    },
    {
        "Asset": "Employee Portal",
        "Type": "Web Application",
        "CVSS": 7.8,
        "Priority": "High",
    },
    {
        "Asset": "Email Server",
        "Type": "Server",
        "CVSS": 6.5,
        "Priority": "High",
    },
])

st.dataframe(
    assets,
    use_container_width=True,
    hide_index=True,
    column_config={
        "CVSS": st.column_config.NumberColumn("CVSS", format="%.1f"),
    },
)

st.caption("CyRIQ · Continuous Cyber Risk Quantification")
