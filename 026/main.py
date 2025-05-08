import random
import pandas

""" List Comprehension
syntax: new_list = [new_item for item in list]
"""
# list
numbers = [1, 2, 3, 4, 5]
new_numbers = [n * 2 for n in numbers]
print(new_numbers)
# string
name = "Handika"
letters_list = [letter for letter in name]
print(letters_list)
# range
numbers2 = [n * 2 for n in range(1, 5)]
print(numbers2)

""" Conditional list comprehension
syntax:
new_list = [new_item for item in list if test]
"""

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

""" Dictionary Comprehension
syntax:
new_dict = {new_key: new_value for item in list}

# Berdasarkan nilai dalam kamus yang sudah ada
new_dict = {new_key: new_value for (key, value) in dict.items()}

# Conditional Dictionary Comprehension
new_dict = {new_key: new_value for (key, value) in dict.items() if test}
"""

student_scores = {name: random.randint(1, 100) for name in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# loop Dataframe
students_data = {
    "student": ["Handika", "Ridho", "Syamsudin", "Rosidahlia"],
    "score": [89, 88, 87, 86]
}

# loop dictionary
# for (key, value) in students_data.items():
#     print(key, value)

students_data_frame = pandas.DataFrame(students_data)

# loop through data frame
# for (key, value) in students_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, value) in students_data_frame.iterrows():
    # print(index)
    print(value["student"], value["score"], sep=": ")