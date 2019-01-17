rows = [
    {'address': '5412 N Clark', 'date': '07/01/2012'},
    {'address': '5148 N Clark', 'date': '07/04/2012'},
    {'address': '5890 E 57th', 'date': '07/02/2012'},
    {'address': '5415 N Clark', 'date': '07/01/2012'},
    {'address': '5143 N Clark', 'date': '07/04/2012'},
    {'address': '5891 E 57th', 'date': '07/02/2012'}

]
from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print('     ', item)


from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for row in rows_by_date['07/01/2012']:
    print(row)
