#Building a Time calculator by Mayra Silva

def format_time(time):
    time = '3:00 PM'
    separator_hours_minutes = ':'
    part_of_the_day = ['AM', 'PM']
    

    splitted_time = time.split()
    print(splitted_time)
    time_of_the_day = splitted_time.pop()
    print(time_of_the_day)
    print(splitted_time)


    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes)
    print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    

format_time('3:00 PM')


def add_time(start, duration, day_of_week=None):
    separator = ':'
    time_of_the_day = ['AM', 'PM']

    start_time = start.split()
    #print(start_time)

    pass


add_time('3:00 PM', '3:10', 'Sunday')