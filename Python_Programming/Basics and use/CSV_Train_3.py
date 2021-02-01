#
import csv
#
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]
with open ("../../Example5.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    for student in students:
        writer.writerow(student)
# Запись списка списков целиком
with open("../../Example5.csv", "a") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(students)
# Запись всех значений в кавычках
with open("../../Example5.csv", "a") as f:
    writer = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writerows(students)
# Запись всех нечисловых значений в кавычках
with open("../../Example5.csv", "a") as f:
    writer = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(students)