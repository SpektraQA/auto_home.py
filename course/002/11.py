import datetime

sample1 = 'Jan 1 2014 2:43 PM'
dt1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M %p')
print(dt1)