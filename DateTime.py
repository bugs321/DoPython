import datetime

x = datetime.datetime(2021,12,18)
print(x)

#print(x.date)
print(x.month)
print(x.year)

y=datetime.datetime.now()

print(y.strftime("%a"))

z=datetime.datetime.today()+timedelta(days=100)
print(z)