#Building a Time calculator by Mayra Silva

def format_time(time):

    separator_hours_minutes = ':'
    

    splitted_time = time.split() #use space as separator
    print(splitted_time)
    time_of_the_day = splitted_time.pop() #remove the string of part of the day (AM, PM)
    print(time_of_the_day)
    print(splitted_time)


    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes) #separate hours and minutes
    print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    if int(minutes) >= 60:
        raise ValueError('Minutes cannot be equal or greater than 60')
    
    splitted_time_hours_and_minutes = splitted_time_hours_and_minutes + [time_of_the_day]
    print(splitted_time_hours_and_minutes)

    return splitted_time_hours_and_minutes
    

format_time('3:00 PM')





def add_time(start, duration, day_of_week=None):
    separator = ':'
    time_of_the_day = ['AM', 'PM']

    start_time = start.split()
    #print(start_time)

    pass


add_time('3:00 PM', '3:10', 'Sunday')