""" this function is a time calculator. The parameters are:
    	- a start time in the 12-hour clock format (ending in AM or PM)
	- a duration time that indicates the number of hours and minutes
	- (optional) a starting day of the week, case insensitive
All these parameters are string inputs.
Here are some paramenters the function can handle and what it is expected to return:

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)"""

def add_time(start_time, duration_time, week_day=0):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if week_day:
        lower_case_week = week_day.casefold()
        week_day = lower_case_week.capitalize()
    else:
        print()

    numbers = start_time.split(":")
    starting_hours = int(numbers[0])
    numbers[1].split()  # the stuff we need
    minutes = (numbers[1].split())[0]
    letters = (numbers[1].split())[1]

    duration_numbers = duration_time.split(":", 1)  # the stuff we nee
    duration_hours = duration_numbers[0]
    duration_minutes = duration_numbers[1]


    # defininng a day
    day, hours = divmod(int(duration_hours), 24)
    total_minutes = int(minutes) + int(duration_minutes)
    # obviously if day < 1 duration hours = hours


    #rememmber that if  total hours + total minutes >12 Pm then day = day +1

    if total_minutes > 59:
        total_minutes = total_minutes - 60
        hours = hours + 1

    if letters == "PM" and (starting_hours + hours) >= 12:
        day = day + 1

    if total_minutes == 0:
        total_minutes = "00"
    if total_minutes < 10:
        total_minutes = "0" + str(total_minutes)

    total_hours = (int(starting_hours) + hours) % 12


    if (hours > 12 and hours > (12 - starting_hours)) or \
    (hours < 12 and hours < (12 - starting_hours)):
        time = str(total_hours) + ":" + str(total_minutes)


        if letters == "AM":
            letters = "AM"
            if total_hours == 0:
                total_hours = total_hours + 12
            time = str(total_hours) + ":" + str(total_minutes)

        if letters == "PM":
            letters = "PM"
        if total_hours == 0:
            total_hours = total_hours + 12
            time = str(total_hours) + ":" + str(total_minutes)
        if day <= 1 and week_day:
            next_day = week.index(week_day) + 1
            new_time = time + " " + str(letters) + ", " + week[next_day]
            if day == 1:
                new_time = new_time + " (next day)"

            if letters == "PM":
                next_day = week.index(week_day) + 1
                new_time = time + " " + str(letters) + ", " + str(week_day)
        elif day <= 1 and week_day == 0:
            if letters == "PM":
                new_time = time + " " + str(letters)
                if day == 1:
                    new_time = new_time + " (next day)"
            else:
                new_time = time + " " + str(letters)
                if day == 1:
                    new_time = new_time + " (next day)"

        elif day > 1 and week_day:
            days_later = ((day % 7) + int(week.index(week_day))) % 7
            new_time = time + " " + str(letters) + ", " + str(week[days_later]) + \
                "  (" + str(day) + " (days later)"
        else:
            if day > 1 and week_day == 0:
                new_time = time + " " + str(letters) + " (" + str(day) + " days later)"

    else:

        if (12 - starting_hours) <= hours <= 12:
            time = str(total_hours) + ":" + str(total_minutes)
            if letters == "AM":
                letters = letters.replace("AM", "PM")
                if total_hours == 0:
                    total_hours = total_hours + 12
                    time = str(total_hours) + ":" + str(total_minutes)
            else:
                if letters == "PM":
                    letters = letters.replace("PM", "AM")
                if total_hours == 0:
                    total_hours = 12
                    time = str(total_hours) + ":" + str(total_minutes)
            if day <= 1 and week_day:
                next_day = week.index(week_day) + 1
                new_time = time + " " + str(letters) + " (next day) " + week[next_day]
                if letters == "PM":
                    new_time = time + " " + week[next_day]
            elif day <= 1 and week_day == 0:
                new_time = time + " " + str(letters) + " (next day)"
                if letters == "PM":
                    new_time = time + " " + str(letters)

            elif day > 1 and week_day:
                days_later = (week.index(week_day) + (day % 7)) % 7
                new_time = time + " " + str(letters) + ", " + str(week[days_later]) + \
                " (" + str(day) + " days later)"
            else:
                if day > 1 and week_day == 0:
                    new_time = time + " " + str(letters) + " (" + str(day) + " days later)"

    return new_time
