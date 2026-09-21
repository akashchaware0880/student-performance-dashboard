import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# DATA
# --------------------------------------------------

data = {
    "Name": [
        "Aakash", "Rahul", "Priya", "Sneha", "Amit",
        "Neha", "Rohit", "Pooja", "Vikas", "Anjali"
    ],
    "Maths": [85, 65, 95, 72, 45, 88, 55, 90, 68, 82],
    "Science": [78, 70, 92, 80, 50, 85, 60, 94, 72, 88],
    "English": [90, 60, 88, 75, 55, 92, 58, 89, 65, 85],
    "Attendance": [92, 75, 98, 85, 60, 95, 68, 97, 78, 90],
    "StudyHours": [4, 2, 6, 3, 1, 5, 2, 6, 3, 4]
}

df = pd.DataFrame(data)

# Calculations
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

df["Rank"] = (
    df["Average"]
    .rank(method="min", ascending=False)
    .astype(int)
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎓 Student Performance Analytics Dashboard")
st.markdown(
    "### Data Science Project | Python • Pandas • Matplotlib • Seaborn • Streamlit"
)

st.divider()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "👨‍🎓 Total Students",
    len(df)
)

col2.metric(
    "📊 Average Marks",
    round(df["Average"].mean(), 2)
)

col3.metric(
    "📅 Avg Attendance",
    f"{df['Attendance'].mean():.1f}%"
)

col4.metric(
    "⏱️ Avg Study Hours",
    f"{df['StudyHours'].mean():.1f} hrs"
)

pass_percentage = (
    (df["Result"] == "Pass").sum() / len(df)
) * 100

col5.metric(
    "✅ Pass Percentage",
    f"{pass_percentage:.0f}%"
)

st.divider()

# --------------------------------------------------
# SIDEBAR FILTER
# --------------------------------------------------

st.sidebar.header("🔎 Student Filter")

selected_student = st.sidebar.selectbox(
    "Select Student",
    ["All Students"] + list(df["Name"])
)

if selected_student != "All Students":
    filtered_df = df[df["Name"] == selected_student]
else:
    filtered_df = df

# --------------------------------------------------
# SELECTED STUDENT
# --------------------------------------------------

if selected_student != "All Students":

    student = filtered_df.iloc[0]

    st.subheader(f"👤 {student['Name']} - Performance")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Average Marks", f"{student['Average']:.2f}")
    c2.metric("Total Marks", student["Total"])
    c3.metric("Attendance", f"{student['Attendance']}%")
    c4.metric("Study Hours", f"{student['StudyHours']} hrs")

    st.divider()

# --------------------------------------------------
# CHART 1 - STUDENT AVERAGE
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Student Average Marks")

    chart_data = df.sort_values(
        "Average",
        ascending=False
    )

    st.bar_chart(
        chart_data.set_index("Name")["Average"]
    )

with col2:

    st.subheader("📚 Subject-wise Average")

    subject_data = pd.DataFrame({
        "Subject": ["Maths", "Science", "English"],
        "Average": [
            df["Maths"].mean(),
            df["Science"].mean(),
            df["English"].mean()
        ]
    })

    st.bar_chart(
        subject_data.set_index("Subject")
    )

# --------------------------------------------------
# CHART 2
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Attendance vs Marks")

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="Attendance",
        y="Average",
        s=100,
        ax=ax
    )

    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Average Marks")

    st.pyplot(fig)

with col2:

    st.subheader("⏱️ Study Hours vs Marks")

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="StudyHours",
        y="Average",
        s=100,
        ax=ax
    )

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Average Marks")

    st.pyplot(fig)

# --------------------------------------------------
# RANKING TABLE
# --------------------------------------------------

st.subheader("🏆 Student Performance Ranking")

ranking = df.sort_values(
    "Rank"
)[
    [
        "Rank",
        "Name",
        "Maths",
        "Science",
        "English",
        "Average",
        "Attendance",
        "StudyHours",
        "Result"
    ]
]

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# CORRELATION
# --------------------------------------------------

st.subheader("🔥 Performance Correlation")

correlation = df[
    [
        "Maths",
        "Science",
        "English",
        "Attendance",
        "StudyHours",
        "Average"
    ]
].corr()

fig, ax = plt.subplots(figsize=(10, 5))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    "**Student Performance Analytics** | "
    "Beginner Data Science Project"
)

st.caption(
    "Built using Python, Pandas, Matplotlib, Seaborn and Streamlit"
)