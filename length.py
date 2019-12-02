import csv
with open("GetTweetUS_attr.csv", newline='', encoding='utf-8') as csv_file:
    for row in csv.reader(csv_file):
        print(len(row))
