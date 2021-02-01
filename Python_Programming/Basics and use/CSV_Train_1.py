#
import csv
#
with open ("../../Example3.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)