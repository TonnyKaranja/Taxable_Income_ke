
import streamlit as st
import pandas as pd
from datetime import date, datetime
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Vspa Management Dashboard", layout="wide")

# ========= HEADER =========
st.title("Vspa Management Dashboard 💅")
st.markdown("Manage and view key data for your spa — services, payments, and staff attendance.")

# ========= NAVIGATION =========
menu = st.sidebar.radio("Select a Section", ["Service Summary", "Staff Attendance"])

# ========= SERVICE SUMMARY =========
if menu == "Service Summary":
    st.header("Service Summary 💆‍♀️")

    service_data = pd.DataFrame({
        "Service": ["Facial", "Massage", "Waxing", "Manicure", "Pedicure"],
        "Staff": ["Alice", "Grace", "Maria", "Jane", "Sarah"],
        "Client": ["Lina", "Diana", "Faith", "Catherine", "Joy"],
        "Payment (KES)": [2500, 4000, 3000, 1500, 2000]
    })

    st.dataframe(service_data)

    st.subheader("Service Summary Chart")
    fig, ax = plt.subplots()
    ax.bar(service_data["Service"], service_data["Payment (KES)"])
    ax.set_ylabel("Payments (KES)")
    ax.set_title("Payments per Service")
    st.pyplot(fig)

    total_earnings = service_data["Payment (KES)"].sum()
    st.metric(label="Total Earnings", value=f"KES {total_earnings}")

# ========= STAFF ATTENDANCE =========
elif menu == "Staff Attendance":
    st.header("Staff Attendance Tracker 👩‍💼")

    attendance_file = "staff_attendance.csv"

    if os.path.exists(attendance_file):
        attendance_df = pd.read_csv(attendance_file)
    else:
        attendance_df = pd.DataFrame(columns=["Date", "Staff Name", "Status", "Clock In Time"])

    st.subheader("Mark Attendance")

    staff_name = st.text_input("Enter Staff Name")
    status = st.selectbox("Select Status", ["Present", "Absent", "On Leave"], key="attendance_status")

    if st.button("Clock In / Save Attendance"):
        if staff_name:
            current_time = datetime.now().strftime("%H:%M:%S")
            new_entry = {
                "Date": date.today(),
                "Staff Name": staff_name,
                "Status": status,
                "Clock In Time": current_time
            }
            attendance_df = pd.concat([attendance_df, pd.DataFrame([new_entry])], ignore_index=True)
            attendance_df.to_csv(attendance_file, index=False)
            st.success(f"{staff_name} marked as {status} at {current_time}")
        else:
            st.warning("Please enter the staff name before saving.")

    st.subheader("Today's Attendance Summary")
    today_data = attendance_df[attendance_df["Date"] == str(date.today())]

    if not today_data.empty:
        st.dataframe(today_data)
    else:
        st.info("No attendance recorded yet for today.")
