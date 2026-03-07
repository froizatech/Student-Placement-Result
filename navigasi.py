import streamlit as st



# Define your pages
home = st.Page("home.py", title="Home")
result = st.Page("datasiswa.py", title="Result Announcement")
visual = st.Page("penyaringan.py", title="Data Visualization")

# Create the navigation bar at the top
pg = st.navigation([home, result, visual], position="top")
pg.run()