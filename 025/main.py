import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = data[data["Primary Fur Color"] == "Gray"].size
cinnamon_squirrels_count = data[data["Primary Fur Color"] == "Cinnamon"].size
black_squirrels_count = data[data["Primary Fur Color"] == "Black"].size

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")


"""
with open("./weather_data.csv", "r") as weather_file:
    data = weather_file.readlines()

print(data)
"""

"""
import csv

temperatures = []

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
"""

# import pandas

# data = pandas.read_csv("./weather_data.csv")

"""
DataFrame adalah struktur data dua dimensi dalam pandas, seperti tabel atau spreadsheet. Berisi baris dan kolom.
"""
# print(data)

# convert dataframe to dictionary
# data_dict = data.to_dict()
# print(data_dict)

"""
Series adalah struktur data satu dimensi dalam pandas. Bisa dianggap seperti kolom pada tabel, atau array 1 dimensi dengan label/index.

temperatures = data["temp"]
print(temperatures.to_list())

avg = temperatures.sum() / temperatures.size
print(avg)

print(temperatures.mean())
print(temperatures.mode())
print(temperatures.median())
print(temperatures.max())
print(temperatures.min())
"""

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data["day"] == "Monday"])
# print(data["temp"] == data["temp"].max())

# monday = data[data.day == "Monday"]
# monday_temp_celc = monday.temp[0]
# monday_temp_fahr = monday_temp_celc * 9/5 + 32
# print(monday_temp_fahr)

# Create a Dataframes from scratch

# student_report = {
#     "students": ["Handika", "Ridho", "Rosidah Lia", "Syamsudin"],
#     "scores": [90, 88, 85, 88],
# }

# data_student = pandas.DataFrame(student_report)
# print(data_student)

# Convert to CSV
# data_student.to_csv("student_report.csv")