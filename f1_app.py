import streamlit as st 
import pandas as pd
import os 
import fastf1 as ff
from time import time
import driver_trace
import trace_options

def yearList():
    yearList = os.listdir("Cache")
    print(yearList.sort())
    return yearList

def raceListGenerator(year):
    raceList = os.listdir(f"Cache/{year}")
    return raceList

schedule = pd.read_parquet("./races_by_year.pq")
yearSel = '2024'
eventList = schedule[schedule['EventYear'] == yearSel]
lapTimingDetails = ""
with st.sidebar:
    with st.form("Base Form"):
        st.write("Enter details")

        yearSel = st.selectbox("Select Year",yearList())
        
        raceSel = st.selectbox("Select Event:", eventList)

        sessionSel = st.selectbox("Select Session:",options=["Race","Qualifying","FP1","FP2", "FP3", "Sprint"])
        
        driverSel = st.text_input("Enter Driver Identifier")
        
        lapSelect = st.text_input("Enter Lap Number", placeholder="Pick Fastest")

        driver2Sel = st.text_input("Add Second Driver for comparison")

        submitted = st.form_submit_button("Submit")

if submitted:
    print(driverSel)
    # lapTimingDetails = driver_trace.plot_traces(int(yearSel), raceSel, sessionSel, driverSel, lapSelect)
    compareDrivers = trace_options.fastestLapTrace(int(yearSel), raceSel, sessionSel, driverSel, driver2Sel)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(lapTimingDetails)

# Once user selects a year, the race dropdown will change
# depending on the races that happened that year
