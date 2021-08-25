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
    cal = calendar.Calendar()
    aaa = [l[days.get(day_of_week)] for l in cal.monthdayscalendar(year, month) if l[days.get(day_of_week)] != 0]

    if week == "teenth":
        bbb = [l for l in aaa if 12 < l < 20][0]
        print(bbb)
        return date(year, month, bbb)

    if week == "last":
        return date(year, month, aaa[-1])

    try:
        bbb = int(week[0]) - 1
        return date(year, month, aaa[bbb])
    except IndexError:
        raise MeetupDayException("invalid index")
