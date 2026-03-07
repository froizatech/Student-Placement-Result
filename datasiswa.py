import streamlit as st
import pandas as pd

df = pd.read_csv("hasil_cleaning_SPL.csv")
df.columns = df.columns.str.strip()

st.subheader("Test Result")

col1, col2 = st.columns([1, 2])

with col1:
    with st.form("student_form"):
        student_id = st.text_input(
            "Student ID",
            value=str(df.loc[0, 'Student_ID'])
        )
        submit = st.form_submit_button("Show Data")

with col2:
    if submit:
        result = df[df['Student_ID'] == int(student_id)]
        if not result.empty:
            row = result.iloc[0]
            placement = row["Placement_Status"]
            st.markdown(f"### Placement Status: **{placement}**")
            if placement == "Placed":
                st.write("Congratulations on your placed result!")
            else:
                st.write("Our deepest apologies...")
            st.dataframe(result, hide_index=True)
        else:
            st.warning("Student ID not found.")

with st.expander("List of Student IDs who have taken the test"):
    student_id_selected = st.selectbox(
        label="Select a Student ID",
        options=df["Student_ID"].unique()
    )