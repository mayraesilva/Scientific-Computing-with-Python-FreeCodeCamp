#Building a Time calculator by Mayra Silva

def format_time(time):
    
    separator_hours_minutes = ':'
    

    splitted_time = time.split() #use space as separator
    #print(splitted_time)
  

    splitted_time_hours_and_minutes = splitted_time[0].split(separator_hours_minutes) #separate hours and minutes
    #print(splitted_time_hours_and_minutes)
    hours = splitted_time_hours_and_minutes[0]
    minutes = splitted_time_hours_and_minutes[1]

    if int(minutes) >= 60:
        raise ValueError('Minutes cannot be equal or greater than 60')
    

    if len(splitted_time) >= 2:
        time_of_the_day = splitted_time.pop() #remove the string of part of the day (AM, PM)
        # print(time_of_the_day)
        # print(splitted_time)
        splitted_time_hours_and_minutes = splitted_time_hours_and_minutes + [time_of_the_day]
    
    #print(splitted_time_hours_and_minutes)


    return splitted_time_hours_and_minutes
    

format_time('3:00 PM')

def calculate_time_passed(moment_of_start, time_of_duration, day_of_week=None):
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    time_of_day = ['AM', 'PM']
    
    period = ''
    hour_model = 0
    days_passed = 0
    new_day_index = 0
    new_time_minutes = 0


    pm_time = { 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 
   19: 7, 20: 8, 21: 9, 22: 10, 23: 11}
    am_time = { 12: 0, 1:  1, 2:  2, 3:  3, 4:  4, 5:  5, 
    6:  6, 7:  7, 8:  8, 9:  9, 10: 10, 11: 11 }


    

    start_hours = int(moment_of_start[0])
    start_minutes = int(moment_of_start[1])
    part_of_the_day = moment_of_start[2]

    hours_passed = int(time_of_duration[0])
    minutes_passed = int(time_of_duration[1])

    

    for time in time_of_day:

        if part_of_the_day == time:

            new_time_minutes = start_minutes + minutes_passed
            new_time_hour = start_hours + hours_passed
            minutes_remain = 0
            print(new_time_hour, 'and', new_time_minutes)

            if new_time_minutes >= 60:

                hours_to_add = new_time_minutes // 60
                minutes_remain = new_time_minutes % 60
                new_time_hour += hours_to_add
                print(new_time_hour, 'and', minutes_remain)


            if new_time_hour >= 24:

                days_passed = new_time_hour // 24
                hour_of_new_day = new_time_hour % 24
                print('This is the hour of new day ', hour_of_new_day)

                if hour_of_new_day == 0:
                    hour_model = 12 #12 AM
                    period = 'AM'
                    print(hour_model, period)
            
                elif 12 <= hour_of_new_day <= 23 :
                    hour_model = pm_time[hour_of_new_day]
                    period = 'PM'
                    print(hour_model, period)

                elif 1 <= hour_of_new_day <= 11:
                    hour_model = am_time[hour_of_new_day]
                    period = 'AM'
                    print(hour_model, period)


                for day in days_of_the_week:

                    if day == day_of_week:

                        print(f'We begin this count on {day_of_week}, now its passed {days_passed} day(s)')
                        new_day_index = days_of_the_week.index(day_of_week) + days_passed

                        if 0 <= new_day_index < 7:
                            print(f"Now it's {days_of_the_week[new_day_index]} ")

                        elif new_day_index >= 7:
                            while new_day_index >= 7:
                                new_day_index = new_day_index - 7
                            print(f"Now it's {days_of_the_week[new_day_index]} ")


    return [hour_model, new_time_minutes, period, days_passed, days_of_the_week[new_day_index] ]


def final_format(info):

    hour = info[0]
    minutes = info[1]
    period = info[2]
    days_passed = info[3]
    new_day = info[4]

    minutes_str = str(minutes)


    if minutes in range(0,10):
        minutes_str = '0' + str(minutes)
    
    time_str = str(hour) + ':' + minutes_str + ' ' + period

    return time_str
        






cases = {
    ('6:30 PM', '00:12'): [7, 42, 'AM'],
    ('6:30 PM', '205:12'): [7, 42, 'AM'],
    ('6:30 PM', '205:12', 'Monday'): [7, 42, 'AM', 'Tuesday'],
}


def add_time(start, duration, day_of_week=None):
    moment_of_start = format_time(start)
    print('Aqui Ó ', moment_of_start)
    time_of_duration = format_time(duration)

    tempo = calculate_time_passed(moment_of_start, time_of_duration, day_of_week)
    print(tempo)
    teste = final_format(tempo)
    print(teste)

    return tempo


for case_input, expected_output in cases.items():
    start, duration = case_input
    day_of_week = expected_output[2] if len(expected_output) > 2 else None
    result = add_time(start, duration, day_of_week)
    print(f"Input: {start}, {duration}, {day_of_week}")
    print(f"Result: {result}")
    print(f"Expected: {expected_output}")
    print("---")

    assert(result == expected_output), f"Test failed for input {case_input}. Expected {expected_output}, but got {result}."