# ============================================================
# STUDENT PERFORMANCE ANALYSIS
# Beginner Data Science Project
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. CREATE STUDENT DATASET
# ------------------------------------------------------------

data = {
    "Name": [
        "Aakash", "Rahul", "Priya", "Sneha", "Amit",
        "Neha", "Rohit", "Pooja", "Vikas", "Anjali"
    ],

    "Maths": [
        85, 65, 95, 72, 45,
        88, 55, 90, 68, 82
    ],

    "Science": [
        78, 70, 92, 80, 50,
        85, 60, 94, 72, 88
    ],

    "English": [
        90, 60, 88, 75, 55,
        92, 58, 89, 65, 85
    ],

    "Attendance": [
        92, 75, 98, 85, 60,
        95, 68, 97, 78, 90
    ],

    "StudyHours": [
        4, 2, 6, 3, 1,
        5, 2, 6, 3, 4
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)


# ------------------------------------------------------------
# 2. DISPLAY ORIGINAL DATA
# ------------------------------------------------------------

print("\n==========================================")
print("       STUDENT PERFORMANCE ANALYSIS")
print("==========================================")

print("\nOriginal Student Data:")
print(df)


# ------------------------------------------------------------
# 3. CHECK DATASET INFORMATION
# ------------------------------------------------------------

print("\n==========================================")
print("DATASET INFORMATION")
print("==========================================")

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
print(df.info())

print("\nChecking missing values:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 4. CALCULATE AVERAGE MARKS
# ------------------------------------------------------------

df["Average"] = df[
    ["Maths", "Science", "English"]
].mean(axis=1)

print("\n==========================================")
print("AVERAGE MARKS")
print("==========================================")

print(
    df[
        ["Name", "Maths", "Science", "English", "Average"]
    ]
)


# ------------------------------------------------------------
# 5. CALCULATE TOTAL MARKS
# ------------------------------------------------------------

df["Total"] = df[
    ["Maths", "Science", "English"]
].sum(axis=1)

print("\n==========================================")
print("TOTAL MARKS")
print("==========================================")

print(df[["Name", "Total"]])


# ------------------------------------------------------------
# 6. PASS / FAIL STATUS
# ------------------------------------------------------------

# Student passes if average marks are 40 or above

df["Result"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)

print("\n==========================================")
print("PASS / FAIL RESULT")
print("==========================================")

print(df[["Name", "Average", "Result"]])


# ------------------------------------------------------------
# 7. FIND TOP STUDENT
# ------------------------------------------------------------

top_student = df.loc[df["Average"].idxmax()]

print("\n==========================================")
print("TOP PERFORMING STUDENT")
print("==========================================")

print("Name:", top_student["Name"])
print("Average Marks:", round(top_student["Average"], 2))
print("Total Marks:", top_student["Total"])


# ------------------------------------------------------------
# 8. FIND LOWEST PERFORMING STUDENT
# ------------------------------------------------------------

lowest_student = df.loc[df["Average"].idxmin()]

print("\n==========================================")
print("LOWEST PERFORMING STUDENT")
print("==========================================")

print("Name:", lowest_student["Name"])
print("Average Marks:", round(lowest_student["Average"], 2))
print("Total Marks:", lowest_student["Total"])


# ------------------------------------------------------------
# 9. SUBJECT-WISE AVERAGE
# ------------------------------------------------------------

math_average = df["Maths"].mean()
science_average = df["Science"].mean()
english_average = df["English"].mean()

print("\n==========================================")
print("SUBJECT-WISE AVERAGE")
print("==========================================")

print("Maths Average:", round(math_average, 2))
print("Science Average:", round(science_average, 2))
print("English Average:", round(english_average, 2))


# ------------------------------------------------------------
# 10. HIGHEST SCORE IN EACH SUBJECT
# ------------------------------------------------------------

print("\n==========================================")
print("HIGHEST SCORE")
print("==========================================")

print("Highest Maths Score:", df["Maths"].max())
print("Highest Science Score:", df["Science"].max())
print("Highest English Score:", df["English"].max())


# ------------------------------------------------------------
# 11. LOWEST SCORE IN EACH SUBJECT
# ------------------------------------------------------------

print("\n==========================================")
print("LOWEST SCORE")
print("==========================================")

print("Lowest Maths Score:", df["Maths"].min())
print("Lowest Science Score:", df["Science"].min())
print("Lowest English Score:", df["English"].min())


# ------------------------------------------------------------
# 12. PASSING STUDENTS
# ------------------------------------------------------------

pass_students = df[df["Result"] == "Pass"]

print("\n==========================================")
print("PASSING STUDENTS")
print("==========================================")

print(pass_students[["Name", "Average", "Result"]])


# ------------------------------------------------------------
# 13. NUMBER OF PASSING AND FAILING STUDENTS
# ------------------------------------------------------------

pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\n==========================================")
print("PASS / FAIL COUNT")
print("==========================================")

print("Number of Passed Students:", pass_count)
print("Number of Failed Students:", fail_count)


# ------------------------------------------------------------
# 14. PASS PERCENTAGE
# ------------------------------------------------------------

pass_percentage = (
    pass_count / len(df)
) * 100

print("\nPass Percentage:",
      round(pass_percentage, 2), "%")


# ------------------------------------------------------------
# 15. STUDENT RANK
# ------------------------------------------------------------

df["Rank"] = (
    df["Average"]
    .rank(method="min", ascending=False)
    .astype(int)
)

df = df.sort_values("Rank")

print("\n==========================================")
print("STUDENT RANKING")
print("==========================================")

print(
    df[
        ["Rank", "Name", "Average", "Total"]
    ]
)


# ------------------------------------------------------------
# 16. STUDY HOURS ANALYSIS
# ------------------------------------------------------------

print("\n==========================================")
print("STUDY HOURS ANALYSIS")
print("==========================================")

print(
    df[
        ["Name", "StudyHours", "Average"]
    ].sort_values(
        "StudyHours",
        ascending=False
    )
)


# ------------------------------------------------------------
# 17. ATTENDANCE ANALYSIS
# ------------------------------------------------------------

print("\n==========================================")
print("ATTENDANCE ANALYSIS")
print("==========================================")

print(
    df[
        ["Name", "Attendance", "Average"]
    ].sort_values(
        "Attendance",
        ascending=False
    )
)


# ------------------------------------------------------------
# 18. CORRELATION
# ------------------------------------------------------------

correlation = df[
    ["Maths", "Science", "English",
     "Attendance", "StudyHours", "Average"]
].corr()

print("\n==========================================")
print("CORRELATION")
print("==========================================")

print(correlation)


# ------------------------------------------------------------
# 19. VISUALIZATION SETTINGS
# ------------------------------------------------------------

sns.set_theme(style="whitegrid")


# ------------------------------------------------------------
# 20. BAR CHART - AVERAGE MARKS
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    df["Name"],
    df["Average"]
)

plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 21. SUBJECT-WISE AVERAGE BAR CHART
# ------------------------------------------------------------

subjects = [
    "Maths",
    "Science",
    "English"
]

subject_averages = [
    math_average,
    science_average,
    english_average
]

plt.figure(figsize=(8, 5))

plt.bar(
    subjects,
    subject_averages
)

plt.title("Subject-Wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 22. ATTENDANCE VS PERFORMANCE
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Average",
    s=100
)

plt.title("Attendance vs Student Performance")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 23. STUDY HOURS VS PERFORMANCE
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="StudyHours",
    y="Average",
    s=100
)

plt.title("Study Hours vs Student Performance")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 24. SUBJECT-WISE BOX PLOT
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df[
        ["Maths", "Science", "English"]
    ]
)

plt.title("Subject Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 25. CORRELATION HEATMAP
# ------------------------------------------------------------

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Performance Correlation")

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 26. SAVE ANALYZED DATA
# ------------------------------------------------------------

df.to_csv(
    "student_performance_result.csv",
    index=False
)

print("\n==========================================")
print("PROJECT COMPLETED")
print("==========================================")

print(
    "\nAnalyzed data has been saved as:"
)

print("student_performance_result.csv")


# ------------------------------------------------------------
# 27. FINAL INSIGHTS
# ------------------------------------------------------------

print("\n==========================================")
print("FINAL INSIGHTS")
print("==========================================")

print(
    "1. Top Student:",
    top_student["Name"]
)

print(
    "2. Highest Subject Average:",
    subjects[
        subject_averages.index(
            max(subject_averages)
        )
    ]
)

print(
    "3. Pass Percentage:",
    round(pass_percentage, 2),
    "%"
)

print(
    "4. Average Attendance:",
    round(df["Attendance"].mean(), 2),
    "%"
)

print(
    "5. Average Study Hours:",
    round(df["StudyHours"].mean(), 2),
    "hours/day"
)

print("\nThank you!")