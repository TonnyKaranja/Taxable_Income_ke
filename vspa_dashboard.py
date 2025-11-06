
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard title
st.title("💆‍♀️ Vspa Service & Payment Dashboard")
st.markdown("Welcome to the Vspa digital service and payment management system mock-up.")

# Sidebar filters
st.sidebar.header("Filter Services")
service_type = st.sidebar.selectbox("Service Type", ["All", "Massage", "Waxing", "Facial", "Nails"])
payment_status = st.sidebar.selectbox("Payment Status", ["All", "Paid", "Pending", "Cancelled"])
staff_name = st.sidebar.selectbox("Staff", ["All", "Mary", "Lydia", "Faith", "Joan"])

# Example service data (includes staff name)
data = {
    "Client Name": ["Alice", "Brenda", "Cynthia", "Diana", "Eva"],
    "Service": ["Massage", "Waxing", "Facial", "Massage", "Nails"],
    "Staff": ["Mary", "Lydia", "Faith", "Joan", "Mary"],
    "Amount (KES)": [2500, 1800, 2000, 2500, 1200],
    "Payment Status": ["Paid", "Pending", "Paid", "Paid", "Pending"],
    "Date": ["2025-11-01", "2025-11-02", "2025-11-03", "2025-11-04", "2025-11-05"]
}

df = pd.DataFrame(data)

# Apply filters
if service_type != "All":
    df = df[df["Service"] == service_type]
if payment_status != "All":
    df = df[df["Payment Status"] == payment_status]
if staff_name != "All":
    df = df[df["Staff"] == staff_name]

# Display data
st.subheader("📋 Service Summary")
st.dataframe(df)

# Payment summary
st.subheader("💰 Payment Overview")
total_revenue = df[df["Payment Status"] == "Paid"]["Amount (KES)"].sum()
pending_amount = df[df["Payment Status"] == "Pending"]["Amount (KES)"].sum()

col1, col2 = st.columns(2)
col1.metric("Total Revenue (KES)", f"{total_revenue:,}")
col2.metric("Pending Payments (KES)", f"{pending_amount:,}")

# Staff performance summary (using Matplotlib)
st.subheader("👩‍🔧 Staff Performance Overview")
staff_summary = df.groupby("Staff")["Amount (KES)"].sum().reset_index()

fig, ax = plt.subplots()
ax.bar(staff_summary["Staff"], staff_summary["Amount (KES)"], color='lightcoral')
ax.set_xlabel("Staff Member")
ax.set_ylabel("Total Earnings (KES)")
ax.set_title("Staff Performance Summary")
st.pyplot(fig)

st.markdown("---")
st.caption("Prototype demo for Vspa Kenya — developed by Antony Karanja.")
