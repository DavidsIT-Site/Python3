from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b
print('{}    {}     {}      {}'.format(c.days, c.seconds, c.seconds/3600, c.total_seconds()/3600))

from datetime import datetime

a = datetime(2018, 1, 25)
print(a + timedelta(days=10))
b = datetime(2019, 1, 25)
d = b-a
print(d.days)

now = datetime.today()
print(now)

print(now + timedelta(minutes=15))