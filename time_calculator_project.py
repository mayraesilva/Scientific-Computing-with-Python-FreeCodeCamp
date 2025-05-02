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

def calculate_time_passed(moment_of_start, time_of_duration, day_of_week=None):
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    time_of_day = ['AM', 'PM']
    #pm_time = {
    #12: 12, 1: 13, 2: 14, 3: 15, 4: 16, 5: 17, 6: 18, 
    #7: 19, 8: 20, 9: 21, 10: 22, 11: 23,
    #}
    
    pm_time = { 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 
   19: 7, 20: 8, 21: 9, 22: 10, 23: 11}

    

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

    if part_of_the_day == 'AM':

        new_time_minutes = start_minutes + minutes_passed
        new_time_hour = start_hours + hours_passed
        minutes_remain = 0
        print(new_time_hour, 'and', new_time_minutes)

        if new_time_minutes >= 60:

            hours_to_add = new_time_minutes // 60
            minutes_remain = new_time_minutes % 60
            new_time_hour += hours_to_add
            print(new_time_hour, 'and', minutes_remain)


        if new_time_hour > 24:

            days_passed = new_time_hour // 24
            hour_of_new_day = new_time_hour % 24
            print('This is the hour of new day ', hour_of_new_day)

            if hour_of_new_day == 0:
                hour_of_new_day = 12 #12 AM
                print(hour_of_new_day)
            
            elif 12 <= hour_of_new_day <= 23 :
                hour_model = pm_time[hour_of_new_day]
                print(hour_model)
            






        




    







def add_time(start, duration, day_of_week=None):
    moment_of_start = format_time(start)
    print('Aqui Ó ', moment_of_start)
    time_of_duration = format_time(duration)

    tempo = calculate_time_passed(moment_of_start, time_of_duration)


    pass


add_time('3:55 AM', '36:10', 'Sunday')