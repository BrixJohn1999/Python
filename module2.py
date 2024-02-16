import datetime
from random import randint

t = datetime.datetime.now()
print(t)

x = datetime.datetime(2024, 2, 16)
print(x.strftime("%B"))
print(x.year)
print(x.day)



print(int(randint(1, 1000)))