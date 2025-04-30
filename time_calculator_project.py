#Building a Time calculator by Mayra Silva

def format_time(time):
    
    separator_hours_minutes = ':'
    

    splitted_time = time.split() #use space as separator
    print(splitted_time)



    
        

    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes) #separate hours and minutes
    print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    if int(minutes) >= 60:
        raise ValueError('Minutes cannot be equal or greater than 60')
    

    if len(splitted_time) >= 2:
        time_of_the_day = splitted_time.pop() #remove the string of part of the day (AM, PM)
        print(time_of_the_day)
        print(splitted_time)
        splitted_time_hours_and_minutes = splitted_time_hours_and_minutes + [time_of_the_day]
    
    print(splitted_time_hours_and_minutes)


    return splitted_time_hours_and_minutes
    

format_time('3:00 PM')

def calculate_time_passed(moment_of_start, time_of_duration):
    time_of_day = ['AM', 'PM']
    pm_time = {
        12 : 12, 1 : 13, 2 : 14, 3 : 15, 4 : 16, 5 : 17, 6 : 18, 7 : 19, 8 : 20, 9 : 21, 10 : 22, 11 : 23,
        }
    

    start_hours = int(moment_of_start[0])
    start_minutes = int(moment_of_start[1])
    part_of_the_day = moment_of_start[2]

    hours_passed = int(time_of_duration[0])
    minutes_passed = int(time_of_duration[1])

    print('Begin test')
    print(start_hours)
    print(part_of_the_day)
    print(start_minutes)
    print('Now duration')
    print(hours_passed)
    print(minutes_passed)



    







def add_time(start, duration, day_of_week=None):
    moment_of_start = format_time(start)
    print('Aqui Ó ', moment_of_start)
    time_of_duration = format_time(duration)

    tempo = calculate_time_passed(moment_of_start, time_of_duration)


    pass


add_time('3:00 PM', '6:10', 'Sunday')