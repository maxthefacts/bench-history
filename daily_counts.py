def daily_counts(df, bench, save_directory_path):
    
    #pivot df on date
    by_day = df.groupby('date').count().reset_index()

    #mean and median of daily counts
    by_day_mean = by_day.measured_at.mean()
    by_day_median = by_day.measured_at.median()
    
    #distribution of means figure
    fig = plt.figure(figsize=(8,6))
    plt.hist(by_day.measured_at, bins = 40)
    plt.title('Distribution of Daily Probe Counts \n Bench: ' + str(bench), size = 24)
    plt.xlabel('Distirbution of Daily Avg')
    plt.ylabel('Number of Days')
    fig.savefig(str(save_directory_path) + '/' + str(bench) + '_dailyMeansDistributions.png')

    return by_day_mean, by_day_median, by_day