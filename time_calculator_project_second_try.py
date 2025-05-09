#Building a Time calculator by Mayra Silva - Secon Try
def format_time(time):
    
    separator_hours_minutes = ':'
    splitted_time = time.split() #use space as separator
   

    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes) #separate hours and minutes
    print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    if int(minutes) >= 60:
        raise ValueError('Minutes cannot be equal or greater than 60')
    

    if len(splitted_time) >= 2:
        time_of_the_day = splitted_time.pop() #remove the string of part of the day (AM, PM)
        splitted_time_hours_and_minutes = splitted_time_hours_and_minutes + [time_of_the_day]
    
    #print(splitted_time_hours_and_minutes)


    return splitted_time_hours_and_minutes




#Receives a list with time in am/pm format and transforme it into 24hrs (list)
def convert_time_24(time_am_or_pm): 

    hour = time_am_or_pm[0]
    minutes = time_am_or_pm[1]    
    part_of_day_started = time_am_or_pm[2]


    pm_time = { 12: 12, 1: 13, 2: 14, 3: 15, 4: 16, 5: 17, 6: 18, 
    7: 19, 8: 20, 9: 21, 10: 22, 11: 23}

    time_converted_24 = []

    if part_of_day_started == 'AM':

        if hour == '12':

            hour = 0
            minutes = int(minutes)
            time_converted_24.append(hour)
            time_converted_24.append(minutes)


        else:
            hour = int(hour)
            minutes = int(minutes)
            time_converted_24.append(hour)
            time_converted_24.append(minutes)

    elif part_of_day_started == 'PM':

        hour = int(hour)
        minutes = int(minutes)

        if hour in pm_time.keys():
            hour = pm_time[hour]
            #print('new hour ', hour)
            time_converted_24.append(hour)
            time_converted_24.append(minutes)

    return time_converted_24






print(convert_time_24(format_time('6:00 AM')))
print(convert_time_24(format_time('3:00 PM')))