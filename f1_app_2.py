import streamlit as st 
import polars as pl
import pandas as pd
import os 
import fastf1 as ff
from time import time

def yearList():
    yearList = os.listdir("Cache")
    print(yearList.sort())
    return yearList

def eventListGenerator(year):
    eventList = os.listdir(f"Cache/{year}")
    eventListClean = eventList
    for i in range(len(eventList)):
        eventListClean[i] = eventList[i][11:].replace("_"," ")
    print(eventListClean)
    return eventListClean

def getSessions():
    session

with st.form("Base Form"):
    st.write("Enter details")
    placeholder = st.empty()
    yearSel = st.selectbox("Select Year",yearList())
    submitYear = st.form_submit_button("Fetch Events")
    if submitYear:
        eventSel = st.selectbox("Select Event:", eventListGenerator(yearSel))
        submitEvent = st.form_submit_button("Fetch Sessions")
        if submitEvent:
            eventSel = st.selectbox("Select Session")
    