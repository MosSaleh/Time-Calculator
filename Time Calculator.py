def add_time(start, duration, weekday=False):
    start_pieces = start.split(":")

    start_hour = start_pieces[0]

    start_pieces = start_pieces[1].split()

    start_mins = start_pieces[0]
    start_AMorPM = start_pieces[1]

    duration_pieces = duration.split(":")
    added_hours = duration_pieces[0]
    added_mins = duration_pieces[1]

    # function to calculate the final minutes and gives an extra hour where applicable
    def minute_calculator():
        extrahour = 0
        fin_min = int(start_mins) + int(added_mins)
        fin_min = int(fin_min)
        if fin_min > 60:
            fin_min = fin_min - 60
            extrahour = 1
        if fin_min < 10:
            fin_min = "0" + str(fin_min)
        return fin_min, extrahour

    fin_min, extrahour = minute_calculator()

    def daylater(start_hour):
        start_hour = int(start_hour)
        if start_AMorPM == "PM":
            start_hour = start_hour + 12
        days = (int(added_hours) + int(start_hour) + extrahour) / 24
        wholedays = int(days)
        dayslater = ""
        if wholedays == 1:
            dayslater = " (next day)"
        if wholedays > 1:
            dayslater = " (" + str(wholedays) + " days later)"
        if wholedays < 1:
            days = 0
        return dayslater, days, start_hour, wholedays

    dayslater, days, start_hour, wholedays = daylater(start_hour)

    def finalhours():
        finalhour = int(added_hours) + start_hour + extrahour - wholedays * 24

        if days >= 1:
            if days - wholedays <= 0.5:
                final_AMorPM = "AM"
            else:
                final_AMorPM = "PM"
        if days < 1:
            if finalhour >= 12:
                final_AMorPM = "PM"
            else:
                final_AMorPM = "AM"
        if finalhour > 12:
            finalhour = finalhour - 12
        if finalhour == 0:
            finalhour = 12

        return finalhour, final_AMorPM

    finalhour, final_AMorPM = finalhours()

    daysofweek = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    new_time = (
        str(finalhour) + ":" + str(fin_min) + " " + str(final_AMorPM) + (dayslater)
    )

    def dayofweek(weekday):
        x = 0
        finalday = ""
        weekday = weekday.lower().strip()
        index = daysofweek.index(weekday)
        for i in range(wholedays):
            index += 1
            if index == 7:
                index = 0
        finalday = daysofweek[index]
        finalday = finalday.capitalize()
        return finalday

    if weekday is not False:
        finalday = dayofweek(weekday)
        new_time = (
            str(finalhour)
            + ":"
            + str(fin_min)
            + " "
            + str(final_AMorPM)
            + ", "
            + finalday
            + (dayslater)
        )

    return new_time
