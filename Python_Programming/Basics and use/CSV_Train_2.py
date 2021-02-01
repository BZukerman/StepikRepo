#
import csv
#
with open ("../../Example4.tsv") as f:
    reader = csv.reader(f, delimiter = "\t")
    for row in reader:
        print(row)