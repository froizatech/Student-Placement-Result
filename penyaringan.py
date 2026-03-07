import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv("hasil_cleaning_SPL.csv")

tab2, = st.tabs(["Data Visualization"])

# TAB 2 - VISUALIZATION

with tab2:

    st.header("Student Data Visualization")

    # Filter in the main page
    col1, col2 = st.columns(2)

    with col1:
        selected_gender = st.selectbox(
            "Select Gender",
            ["All"] + list(df["Gender"].unique())
        )

    with col2:
        selected_degree = st.selectbox(
            "Select Degree",
            ["All"] + list(df["Degree"].unique())
        )


    # Data filtering

    filtered_df = df.copy()

    if selected_gender != "All":
        filtered_df = filtered_df[filtered_df["Gender"] == selected_gender]

    if selected_degree != "All":
        filtered_df = filtered_df[filtered_df["Degree"] == selected_degree]

    st.divider()

    st.write(f"Total Students: {len(df['Student_ID'])} Students")
    male_df = df[df['Gender'] == 'Male']
    female_df = df[df['Gender'] == 'Female']

    st.write(f"Total Male Students: {len(male_df)} Students")
    st.write(f"Total Female Students: {len(female_df)} Students")

    # BAR CHART AGE

    st.subheader("Age Distribution")

    fig1, ax1 = plt.subplots()
    filtered_df["Age"].value_counts().sort_index().plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Total Students")
    st.pyplot(fig1)

    
    # BAR CHART BRANCH

    st.subheader("Branch Distribution")

    fig2, ax2 = plt.subplots()
    filtered_df["Branch"].value_counts().plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Branch")
    ax2.set_ylabel("Total")
    st.pyplot(fig2)

    
    # HISTOGRAM CGPA
    
    st.subheader("CGPA Distribution")

    fig3, ax3 = plt.subplots()
    ax3.hist(filtered_df["CGPA"], bins=10)
    ax3.set_xlabel("CGPA")
    ax3.set_ylabel("Frequency")
    st.pyplot(fig3)

    
    # BAR CHART PLACEMENT STATUS
    
    st.subheader("Placement Status")

fig4, ax4 = plt.subplots()

counts = filtered_df["Placement_Status"].value_counts()
bars = ax4.bar(counts.index, counts.values)

ax4.set_xlabel("Placement Status")
ax4.set_ylabel("Total Students")

# Adding number above the bar chart
for bar in bars:
    height = bar.get_height()
    ax4.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha='center',
        va='bottom'
    )

st.pyplot(fig4)