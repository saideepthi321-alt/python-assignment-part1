# Task 1 - Data Parsing & Profile Cleaning
# given raw student data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# creating empty list to store cleaned student data
cleaned_students = []

# Step 1: Clean and store data
for student in raw_students:
    
    # remove extra spaces and convert name to proper format
    clean_name = student["name"].strip().title()

    # convert roll number from string to integer
    clean_roll = int(student["roll"])

    clean_marks = []
    # convert marks string into list of integers
    marks_list = student["marks_str"].split(", ")
    for m in marks_list:
        clean_marks.append(int(m))

    #create new cleaned data
    cleaned = {
        "name": clean_name, 
        "roll": clean_roll, 
        "marks": clean_marks
    }

    # add cleaned data to list
    cleaned_students.append(cleaned)


# Step 2: processing cleaned data
target_name = None

for student in cleaned_students:
    name = student["name"]
    roll = student["roll"]
    marks = student["marks"]

    # check if name contains only alphabets
    is_valid = all(word.isalpha() for word in name.split())

    # print validation result 
    if is_valid: 
        print("✓ Valid name") 
    else: 
        print("✗ Invalid name")

    # printing student details in required format
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

# Step 3: After processing all students
# find student with roll number 103 and print name in different formats
for student in cleaned_students:
    if student["roll"] == 103:
        print("Uppercase:", student["name"].upper())
        print("Lowercase:", student["name"].lower())



#Task 2 - Marks Analysis Using Loops & Conditionals
# Initial Data
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\nStudent Name:", student_name)

print("\n--- Subject Marks and Grades ---")

# 1. using for loop to go through each subject
for i in range(len(subjects)):
    score = marks[i] # getting marks of each subject

    # checking grade based on marks
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    # printing subject, marks and grade
    print(subjects[i], ":", score, "-", grade)

#2.calculations
#calculating total marks
total_marks = sum(marks)

# calculating average marks
average_marks = round(total_marks / len(marks), 2)

# finding highest and lowest marks
max_marks = max(marks)
min_marks = min(marks)

# finding index position of highest and lowest marks
max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("\n--- Summary ---")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Scoring Subject:", subjects[max_index], "(", max_marks, ")")
print("Lowest Scoring Subject:", subjects[min_index], "(", min_marks, ")")

# 3. While loop: Marks entry system
print("\n--- Add New Subjects ---")

# counter to count how many new subjects added
new_subject_count = 0

while True:
    # asking user to enter subject name
    subject = input("Enter subject name (or type 'done' to stop): ")

    # checking if user wants to stop
    if subject.lower() == "done":
        break

    # asking marks for that subject
    marks_input = input(f"Enter marks for " + subject + " (0–100): ")

    # checking if input is number or not
    if not marks_input.isdigit():
        print("do not crash, and do not add invalid entries to the list.")
        continue    # skip and go to next loop

    marks_value = int(marks_input) # converting string to integer

    # checking if marks are within valid range
    if marks_value < 0 or marks_value > 100:
        print("do not crash, and do not add invalid entries to the list.")
        continue    # skip and go to next loop

    # adding valid subject and marks to list
    subjects.append(subject)
    marks.append(marks_value)
    # increasing counter
    new_subject_count += 1

print("\n--- Updated Summary ---")
print("New subjects added:", new_subject_count)

# Updated average
updated_average = round(sum(marks) / len(marks), 2)
print("Updated Average Marks:", updated_average)



# Task 3 - Class Performance Summary

# given class data (list of tuples)
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# variables to track pass/fail count
pass_count = 0
fail_count = 0

# to find topper
topper_name = ""
topper_avg = 0

# to calculate class average later
total_avg_sum = 0

# printing table header
print("Name                | Average | Status")
print("-" * 40)

# loop through each student in class_data
for student in class_data:
    
    name = student[0]     # get student name
    marks = student[1]    # get list of marks
    
    # calculate average marks
    avg = sum(marks) / len(marks)
    
    # round to 2 decimal places
    avg = round(avg, 2)
    
    # add to total average sum (for class average later)
    total_avg_sum = total_avg_sum + avg
    
    # decide pass or fail
    if avg >= 60:
        status = "Pass"
        pass_count = pass_count + 1   # increase pass count
    else:
        status = "Fail"
        fail_count = fail_count + 1   # increase fail count
    
    # check if this student is topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    # print formatted row
    print(f"{name:<18} | {avg:>7.2f} | {status}")

# calculate class average
class_average = total_avg_sum / len(class_data)
class_average = round(class_average, 2)

# print summary
print("\nSummary:")
print("Number of students passed:", pass_count)
print("Number of students failed:", fail_count)
print("Class topper:", topper_name, "-", topper_avg)
print("Class average:", class_average)



#Task 4 — String Manipulation Utility

# Given essay
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Remove leading and trailing spaces
# strip() removes spaces from beginning and end
clean_essay = essay.strip()

print("Step 1 - Clean Essay:", clean_essay)


# Step 2: Convert to Title Case
# title() makes first letter of each word capital
title_case = clean_essay.title()

print("Step 2 - Title Case:", title_case)


# Step 3: Count how many times "python" appears
# since text is already lowercase, we can directly count
python_count = clean_essay.count("python")

print("Step 3 - Count of 'python':", python_count)

# Step 4: Replace "python" with "Python 🐍"
# replace() changes all occurrences
replaced_text = clean_essay.replace("python", "Python 🐍")

print("Step 4 - Replaced Text:", replaced_text)

# Step 5: Split into sentences
# splitting using ". " (dot + space)
sentences = clean_essay.split(". ")

print("Step 5 - List of Sentences:", sentences)


# Step 6: Print each sentence on new line with numbering
print("Step 6 - Numbered Sentences:")

for i, sentence in enumerate(sentences, start=1):
    
    # check if sentence already ends with '.'
    if not sentence.endswith("."):
        sentence = sentence + "."
    
    # print with numbering
    print(f"{i}. {sentence}")