from datetime import datetime, timedelta
now = datetime.now()
print(datetime.strftime(now, '%d/%m/%y %H:%M:%S.%f'))
yesterday = now - timedelta(days=7)
print(yesterday)
one_month_ago = now - timedelta(days=31)
print(one_month_ago)
str_date = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(str_date, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)