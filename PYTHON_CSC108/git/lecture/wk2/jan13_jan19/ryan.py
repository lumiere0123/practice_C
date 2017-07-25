# How fast was your marathon?
hours = 4
minutes = 12

# Figure out our time in minutes and convert it to Ryan time.
time_in_minutes = hours * 60 + minutes
ryan_time_in_minutes = time_in_minutes * 0.7

# Convert Ryan time back to hours and minutes.
ryan_hours = ryan_time_in_minutes // 60
ryan_minutes = ryan_time_in_minutes % 60

print('Your ryan time is: ')
print('Hours: ', ryan_hours)
print('Minutes: ', ryan_minutes)