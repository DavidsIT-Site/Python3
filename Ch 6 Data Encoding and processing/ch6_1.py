# reading and writing csv file
import csv
with open('CSVData_1.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

from collections import namedtuple
with open('Stock1.csv', encoding='utf-8-sig') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    print(headings)
    Row = namedtuple('Row', headings)
    for pos in f_csv:
        row = Row(*pos)
        print("\t{:7} {} {:10} {:7} {:10.5} {:1.9}".format(row.Symbol, row.Price, row.Date, row.Time, row.Change, row.Volume))
