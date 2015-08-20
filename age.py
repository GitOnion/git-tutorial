import datetime
born = datetime.datetime(1986,4,25)
now = datetime.datetime.now()
diff = now - born
datetime.timedelta(born, now)
