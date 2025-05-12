#Building a Time calculator by Mayra Silva - Second Try
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







#Receives a list with time in 24hrs format and transforme it into am/pm  (list)
def convert_time_am_or_pm(time_24hrs_format):

    hour = time_24hrs_format[0]
    minutes = time_24hrs_format[1]


    pm_time_to_am = {12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 
   19: 7, 20: 8, 21: 9, 22: 10, 23: 11}
    
    time_converted_am_or_pm = []


    if hour <= 11:

        if hour == 0:

            hour = 12

            time_converted_am_or_pm.append(hour)
            time_converted_am_or_pm.append(minutes)
            time_converted_am_or_pm.append('AM')

        else:
            time_converted_am_or_pm.append(hour)
            time_converted_am_or_pm.append(minutes)
            time_converted_am_or_pm.append('AM')

    elif hour >= 12:
        if hour in pm_time_to_am.keys():

            hour = pm_time_to_am[hour]

            time_converted_am_or_pm.append(hour)
            time_converted_am_or_pm.append(minutes)
            time_converted_am_or_pm.append('PM')


    return(time_converted_am_or_pm)








def calculate_time_passed(start, duration):

    hour_started = start[0]
    minutes_started = start[1]
    hours_passed = duration[0]
    minutes_passed = duration[1]

    
    days_passed = 0
    new_hour = []


    total_hour = hour_started + hours_passed
    total_minutes = minutes_started + minutes_passed

    if total_minutes >= 60:

        hours_to_add =  total_minutes // 60
        total_minutes = total_minutes % 60
        total_hour = total_hour + hours_to_add


    if total_hour >=24:

        days_passed = total_hour // 24
        total_hour = total_hour % 24



    new_hour.append(total_hour)
    new_hour.append(total_minutes)

    if days_passed > 0:
        new_hour.append(days_passed)

    return new_hour





def day_of_week(start_day, days_passed=0):

    days_of_week = {
    "sunday":    "Sunday",
    "monday":    "Monday",
    "tuesday":   "Tuesday",
    "wednesday": "Wednesday",
    "thursday":  "Thursday",
    "friday":    "Friday",
    "saturday":  "Saturday",
    }


    days_of_week_index = list(days_of_week.keys())
    new_day = ''
    start_day = start_day.lower()



    if start_day in days_of_week.keys():
        print(f'We are starting on {days_of_week[start_day]}')


    if days_passed == 1:
        new_day = '(next day)'


    elif days_passed >= 2:

        index_of_day = days_of_week_index.index(start_day)
        index_of_new_day = index_of_day + days_passed


        while index_of_new_day >= 7:
            index_of_new_day = (index_of_new_day % 7) 
            new_day = days_of_week[days_of_week_index[index_of_new_day]]
            #print('This is the new day ', new_day)

    return new_day










    





#Test zone

hour_in_24_am = [0, 30]
hour_in_24_pm = [18, 45]

print(convert_time_24(format_time('6:00 AM')))
print(convert_time_24(format_time('3:00 PM')))

print('teste 1 ',convert_time_am_or_pm(hour_in_24_pm) )
convert_time_am_or_pm(hour_in_24_pm)
print('teste 2 ', convert_time_am_or_pm(hour_in_24_am))

print('See how calculation works', calculate_time_passed([23, 40],[24, 30] ))
print('second conversion test', convert_time_am_or_pm(calculate_time_passed([23, 40],[24, 30] )))


print(day_of_week('Wednesday', 30))