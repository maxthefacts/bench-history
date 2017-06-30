def dignostic (source_directory_path, serial_number, save_directory_path):
    df = ingest_for_summary(source_directory_path, serial_number, save_directory_path)
    single_probes_percent, too_common_mac_IDs_percent, all_unique_mac_ids, df = drop_too_few_too_many(df)
    by_day_mean, by_day_median, by_day = daily_counts(df, serial_number, save_directory_path)
    day_types = weekday_counts(df, save_directory_path, serial_number)
    downdays, updays, percent_up, date_range = UpAndDownTimes(df)
    last_thirty_downdays, last_thirty_updays, percent_last_thirty_days = LastThirtyDays(date_range, by_day)
    
    
    
    
    #summerize and save as csv
    summary = pd.DataFrame([single_probes_percent, too_common_mac_IDs_percent, all_unique_mac_ids, by_day_mean,
             by_day_median, downdays, updays, percent_up, last_thirty_downdays, last_thirty_updays, percent_last_thirty_days]).T

    summary.columns = ['Percent Single Probes', 'Percent Too Common Probes', 'Total Unique Mac Addresses', 'Daily Mean MacIds',
                   'Daily Median MacIDs', 'Days Down', 'Days Up', 'Percent of Time Up', 'Last 30 Days Down', 'Last 30 Days Up',
                      'Last Thirty Days Percent']
    summary.to_csv(str(save_directory_path) + '/' + str(serial_number) + '_summaryDignostics.csv')
    
    #
    day_types.to_csv(str(save_directory_path) + '/' + str(serial_number) + '_weekdayMeansAndMedians.csv')
    
    #
    by_day = by_day[['date', 'measured_at']]
    by_day.columns = ['date', 'Unique Probes']
    by_day.to_csv(str(save_directory_path) + '/' + str(serial_number) + '_dailyCounts.csv')