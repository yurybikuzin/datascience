from datetime import datetime, timedelta

date_string = '05.05.2019 21:00'

dt = datetime.strptime(date_string, '%d.%m.%Y %H:%M')
print(dt, dt.hour)
print(dt.month)

dt = datetime(2019, 5, 5, 21, 0)

print(dt.strftime('%Y-%m-%d'))
dt = datetime(2019, 4, 1, 18, 59, 44)
print(dt.strftime('%Y-%m-%d'))

# from datetime import datetime
date_string = '2019-07-07T18:59:33'
date_format = datetime.strftime(datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S'), '%d.%m.%Y')
print(date_format)

dt_list = ['2019-07-07T18:59:06', '2019-07-07T19:00:02', '2019-07-07T19:01:04']
datetime_list = list(map(lambda dt: datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S'), dt_list))
print(datetime_list)

report_seconds = list(map(lambda dt: (dt - datetime.strptime(datetime.strftime(dt ,'%Y-%m-%dT%H:%M'), '%Y-%m-%dT%H:%M')).seconds, datetime_list))
print(report_seconds)

total_time = sum(report_seconds)
print(total_time)

start_date = '2019-01-01'
start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
print(start_date_datetime + timedelta(days = 1))
print(start_date_datetime + timedelta(days = -7))
start_date_datetime += timedelta(hours = 1)
print(start_date_datetime)

start_date = '2019-01-01'
end_date = '2019-01-07'
start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
end_date_datetime = datetime.strptime(end_date, '%Y-%m-%d')
print(start_date_datetime, end_date_datetime)

current_day = start_date_datetime
current_day = start_date_datetime
while current_day <= end_date_datetime:
    print(current_day.strftime('%Y-%m-%d'))
    current_day += timedelta(days=1)

