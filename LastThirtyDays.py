def LastThirtyDays(date_range, by_day):
    last_thirty = date_range[-31:-1]
    last_thirty_by_day = by_day[by_day.date.isin(last_thirty)]
    last_thirty_downdays = len(set(last_thirty) - set(last_thirty_by_day.date))
    last_thirty_updays = 30 - last_thirty_downdays
    percent_last_thirty_days = last_thirty_updays / float(30)
    
    return last_thirty_downdays, last_thirty_updays, percent_last_thirty_days