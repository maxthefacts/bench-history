def weekday_counts(df, save_directory_path, bench):
    
    #loop through each day of tbe week and find mean, median for each day
    day_types = []
    for day_type in df.weekday.unique():
        temp = df[df['weekday'] == day_type].groupby('date').count()
        temp_mean = temp.measured_at.mean()
        temp_median = temp.measured_at.median()
        day_types.append((day_type, temp_mean, temp_median))
    day_types = pd.DataFrame(day_types, columns = ['day', 'mean', 'median'])
    day_types_to_string = pd.DataFrame(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], columns = ['weekday'])
    day_types_to_string['day'] = [6, 0, 1, 2, 3, 4, 5]
    day_types = day_types.merge(day_types_to_string, how = 'inner', on = 'day')
    
    #create figure for means and median for each day of the week
    fig = plt.figure(figsize=(11,11)) 
    ax = fig.add_subplot(111)
    width = 0.2
    day_types['mean'].plot(kind = 'bar', width=width, position=1, label = 'mean')
    day_types['median'].plot(kind = 'bar', width=width, position=0, label = 'median', color = 'g')
    plt.xticks(range(7), day_types.weekday, size = 20)
    plt.ylabel('Mean Probes', size =20)
    plt.title('Mean (Blue) and Medians (Green) \n of Diffrent Days of the Week \n At ' + str(bench), size = 24)
    fig.savefig(str(save_directory_path) + '/' + str(bench) + '_weekdayMeansAndMedians.png')

    return day_types
    