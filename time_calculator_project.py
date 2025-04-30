#Building a Time calculator by Mayra Silva

def format_time(time):
    time = '3:00 PM'
    part_of_the_day = ['AM', 'PM']

    splitted_time = time.split()
    print(splitted_time)

format_time('3:00 PM')


def add_time(start, duration, day_of_week=None):
    separator = ':'
    time_of_the_day = ['AM', 'PM']

    start_time = start.split()
    #print(start_time)

    pass


add_time('3:00 PM', '3:10', 'Sunday')