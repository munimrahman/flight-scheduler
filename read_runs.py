import csv

with open('./data/run.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        print(line)
        