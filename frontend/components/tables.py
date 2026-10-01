import streamlit as st


def show_asset_table():
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