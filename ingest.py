def ingest_for_summary(source_directory_path, serial_number, save_directory_path):

    print 'Finished Ingesting Raw Data '
    #store today's date
    today_string = str(datetime.today().date())

    #establish the source directory of raw data that comes from backend systems
    directory = source_directory_path

    #ingest raw data into a Pandas DataFrame:

    #open every file in the directory with a .txt filename.  Read it in as a Panda.  Store these pandas in a list.
    #concat these dataframes into a single master dataframe called 'df'
    #depending on number of ingest files, this can take a lot of time

    list_of_dfs = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            try:
                temp_df = pd.read_csv(directory + "/" + filename)
                list_of_dfs.append(temp_df)
            except:
                continue
    df = pd.concat(list_of_dfs)

    ###

    #Take raw strings of timestamps and convert them into a python datetime object.  This allows you to extract the date 
    TIMESTAMPS = []
    dates = []
    for timeStamps in df.measured_at:
        temp_date = datetime.strptime(timeStamps.split('T')[0], "%Y-%m-%d").date()
        temp_time = datetime.strptime(timeStamps.split('T')[1].split('-')[0], "%H:%M:%S").time()
        dates.append(temp_date)
        TIMESTAMPS.append(temp_time)
    df['date'] = dates
    df['time'] = TIMESTAMPS
    df['timestamp'] = df.apply(lambda r : pd.datetime.combine(r['date'],r['time']),1)

    ###

    #To ease aggergation, create seperate columns in the dataframe for day, hour, month, year, 
    #and day of the week (weekday)
    day = []
    hour = []
    month = []
    year = []
    weekday = []
    for timestamps in df.timestamp:
        day.append(timestamps.day)
        hour.append(timestamps.hour)
        month.append(timestamps.month)
        year.append(timestamps.year)
        weekday.append(timestamps.weekday())
    df['year'] = year
    df['month'] = month
    df['day'] = day
    df['hour'] = hour
    df['weekday'] = weekday

    ###

    #store as a pickle to save time in the future
    df.to_pickle(str(save_directory_path) + '/' + str(datetime.today().date()) + '-' + str(serial_number) + '.pkl')
    
    return df