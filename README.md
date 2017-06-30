# Sesnor Histoy Dignostics

### This function, dignostic.py, takes three inputs:
    1) A source_directory_path (full path of where the raw data resides)
    2) The serial number of the device (i.e A30-A23)
    3) A save_directory_path, the full path where you want the files saved

### This script looks at the whole history of a sensor and gives you:
    1) A pickle of a panda for the data
    2) The number of unique Mac Addresses for each bench
    3) The number and percent of probes dropped for being too rare and too common
    4) The median and mean count of mac addresses aggergated daily
    5) The median and mean count of mac addresses aggergated by weekday
    6) The uptime and downtime as percent up and down in days
    7) The last 30 days, uptime, downtime, and percent down
    8) An daily count CSV
    
### Max Feinglass 6-30-2017


 
