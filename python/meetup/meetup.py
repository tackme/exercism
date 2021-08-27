from datetime import date
import calendar

days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    column = [l[days.get(day_of_week)] for l in calendar.monthcalendar(year, month) if l[days.get(day_of_week)] != 0]

    if week == "teenth":
        teenth_day = [l for l in column if 12 < l < 20][0]
        return date(year, month, teenth_day)

    if week == "last":
        return date(year, month, column[-1])

    try:
        index = int(week[0]) - 1
        return date(year, month, column[index])
    except IndexError as e:
        raise MeetupDayException(f"{week.title()} {day_of_week} is in {month}.{year} ") from e
