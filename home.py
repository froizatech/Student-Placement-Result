import pandas as pd
import streamlit as st

df = pd.read_csv("hasil_cleaning_SPL.csv")

st.set_page_config(page_title="F5 Test Website")
with st.container(horizontal_alignment="center"):
    st.image("F5.png")

st.header('Welcome to the F5 Placement Test Website', text_alignment="center")

st.markdown("F5 test 2026. Please go to the Result Announcement tab to view your placement test results.", text_alignment="center")
