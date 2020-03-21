seconds = int(input("insert value of seconds for conversation: "))
#DIVIDER OF YEARS
year = seconds // 31536000
year_rem = seconds % 31536000
#DIVIDER OF DAYS
day = year_rem // 86400
day_rem = year_rem % 86400
#DIVIDER OF HOURS
hour = day_rem // 3600
hour_rem = day_rem % 3600
#DIVIDER OF MINUTES
minute = hour_rem // 60
seconds_rem = hour_rem % 60
#PRINT RESULT
print("{} Year(s) {} Day(s) {} Hour(s) {} Minute(s) {} Second(s)".format(year,day,hour,minute, seconds_rem))
