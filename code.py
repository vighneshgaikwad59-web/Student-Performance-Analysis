import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/students.csv")

# Calculate total and average
df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Find grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Display student data
print("\n--- Student Performance ---")
print(df)

# Top student
top_student = df.loc[df["Average"].idxmax()]

print("\n--- Top Student ---")
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))
print("Grade:", top_student["Grade"])

# Subject averages
print("\n--- Subject Averages ---")
print("Maths:", df["Maths"].mean())
print("Science:", df["Science"].mean())
print("English:", df["English"].mean())

# Number of students in each grade
print("\n--- Grade Distribution ---")
print(df["Grade"].value_counts())

# Save updated data
df.to_csv("output/student_results.csv", index=False)

# Create chart
df[["Maths", "Science", "English"]].mean().plot(
    kind="bar",
    title="Average Marks by Subject"
)

plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("output/subject_average.png")
plt.show()
