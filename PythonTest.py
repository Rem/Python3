def readble_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    print("{} week(s) and {} days(s)".format(weeks, remainder))


readble_timedelta(10)
