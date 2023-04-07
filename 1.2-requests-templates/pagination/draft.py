import csv
from pprint import pprint

with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
    stantions = []
    f_reader = csv.DictReader(f)
    stantion = []
    for row in f_reader:
        stantions.append(row.items())
    for lst in stantions:
        stantion = list(lst)
        pprint(stantion)