
import streamlit as st
import pandas as pd
from datetime import date

st.title("🕒 Staff Attendance Tracker")

# Input fields
staff_name = st.selectbox("Select Staff", ["Nancy", "Cynthia", "Lydia"], key="staff_select")
status = st.selectbox("Select Status", ["Present", "Absent", "Off Duty"], key="status_select")
attendance_date = st.date_input("Select Date", value=date.today(), key="date_input")



        
