import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Asset Inventory",
    page_icon="🗂️",
    layout="wide"
)

st.title("🗂️ Asset Inventory")

st.write(
    "View and monitor all important assets of the organization."
)

st.divider()

assets = [
    {
        "Asset Name": "Customer Database",
        "Asset Type": "Database",
        "Criticality": 9,
        "Value": "₹20 Lakh",
        "Status": "Active"
    },
    {
        "Asset Name": "Payment Server",
        "Asset Type": "Server",
        "Criticality": 10,
        "Value": "₹30 Lakh",
        "Status": "Active"
    },
    {
        "Asset Name": "Employee Portal",
        "Asset Type": "Web Application",
        "Criticality": 7,
        "Value": "₹10 Lakh",
        "Status": "Active"
    },
    {
        "Asset Name": "Email Server",
        "Asset Type": "Server",
        "Criticality": 6,
        "Value": "₹8 Lakh",
        "Status": "Active"
    }
]

df = pd.DataFrame(assets)

st.subheader("All Assets")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("Asset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Assets", len(df))

with col2:
    st.metric(
        "Critical Assets",
        len(df[df["Criticality"] >= 9])
    )

with col3:
    st.metric(
        "High Risk Assets",
        len(df[df["Criticality"] >= 7])
    )