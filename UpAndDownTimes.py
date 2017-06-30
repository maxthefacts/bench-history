def UpAndDownTimes(df):
    
    #find the first day we have data for
    start = df.date.min()
    
    #today is the end of the date range
    end = datetime.now().date()
    delta = end - start
    date_range = []
    
    #create a list of all days in range
    for i in range(delta.days+1):
        date_range.append(start + timedelta(days=i))
    
    #find the number of downdays by comapring the number of days in range with the number of days we have data for
    total_days = (end - start).days
    downdays = len(set(date_range) - set(by_day.date))
    updays = total_days - downdays
    percent_up = (updays / float(total_days))
    
    return downdays, updays, percent_up, date_range