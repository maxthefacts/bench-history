def drop_too_few_too_many (df):
        
    # Drop Mac Addresses that occur a single time
    start = len(df)
    # keep only Mac_Addresses that occur more than once in the dataframe
    df = df.loc[df.duplicated(subset='mac_address', keep=False), :]
    end = len(df)
    single_probes_percent = (start - end)/float(start)

    
    ###
    
    # Drop Mac Adresses that occur less than a 3000 times.
    drop_threshhold = 3000
    
    # A few Mac_IDs account for the lions share of all probes.  Throw these out as they are unlikely to be a human phone which 
    # is the assumption of the exercise.  I arbitrarily selected 3000 probes over a trend period as this is likely more than 6 times a day,
    # every day, without exception.  This criteria should be updated to a more sophisticated threshold when time allows.
    # One can find outliers in the probe frequency per mac_ID and , evaluate if they are phones or not, and then throw out non-cell phones
    
    #pivot dataframe on Mac_IDs
    mac_ID_counts = df.groupby('mac_address').count().reset_index()
    #only select Mac_IDs with counts below the threshold
    too_common_mac_IDs = list(mac_ID_counts[mac_ID_counts.measured_at >= (drop_threshhold)].mac_address)
    # Drop the too_common_mac_IDs from the dataframe
    df = df[~df['mac_address'].isin(too_common_mac_IDs)]
    too_common_mac_IDs_percent = len(too_common_mac_IDs)/ float(start)                                                         
    
    ###                                                           
                                                               
    # count remaining unique MacIds
    all_unique_mac_ids = df.mac_address.unique()
    
    return single_probes_percent, too_common_mac_IDs_percent, len(all_unique_mac_ids), df
                                                               