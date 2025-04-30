#Building a Time calculator by Mayra Silva

def format_time(time):
    
    separator_hours_minutes = ':'
    

    splitted_time = time.split() #use space as separator
    print(splitted_time)



    if len(splitted_time) >= 2:
        time_of_the_day = splitted_time.pop() #remove the string of part of the day (AM, PM)
        print(time_of_the_day)
        print(splitted_time)
        

    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes) #separate hours and minutes
    print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    if int(minutes) >= 60:
        raise ValueError('Minutes cannot be equal or greater than 60')
    

    if len(splitted_time) >= 2:
        splitted_time_hours_and_minutes = splitted_time_hours_and_minutes + [time_of_the_day]
    
    print(splitted_time_hours_and_minutes)

    return splitted_time_hours_and_minutes
    

format_time('3:00 PM')

def calculate_time_passed(moment_of_start, time_of_duration):
    time_of_day = ['AM', 'PM']

    start_hours = moment_of_start[0]
    start_minutes = moment_of_start[1]

    







def add_time(start, duration, day_of_week=None):
    moment_of_start = format_time(start)
    time_of_duration = format_time(duration)

    pass


#add_time('3:00 PM', '3:10', 'Sunday')