import csv

with open('WGUPS Package File.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    with open('WGUPS Package File.csv', mode = 'w') as outfile:
        writer = csv.writer(outfile)
        dict = {rows[0]: rows[1] for rows in reader}