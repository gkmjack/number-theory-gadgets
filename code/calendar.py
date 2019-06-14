day_index = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
};

century_offset = {
    0: 5, # 1999-12-31 is Friday
    1: 4, # 2099-12-31 is Thursday
    2: 2, # 2199-12-31 is Tuesday
    3: 0, # 2299-12-31 is Sunday
};

month_offset = {
    1:  0,
    2:  3,
    3:  3,
    4:  6,
    5:  1,
    6:  4,
    7:  6,
    8:  2,
    9:  5,
    10: 0,
    11: 3,
    12: 5,
};

month_length = {
    1:  31,
    2:  28,
    3:  31,
    4:  30,
    5:  31,
    6:  30,
    7:  31,
    8:  31,
    9:  30,
    10: 31,
    11: 30,
    12: 31,
};

def is_leap_year(year):
    c = year // 100;
    y = year % 100;
    if (y == 0):
        return (c%4 == 0);
    else:
        return (y%4 == 0);

def is_valid_date(year, month, day):
    if (not isinstance(year, int) or year < 1):
        return False;
    if (month < 1 or month > 12):
        return False;
    max_day = month_length[month];
    if (is_leap_year(year) and month == 2):
        max_day += 1;
    if (day < 1 or day > max_day):
        return False;
    return True;


def day_of_the_week(year, month, day):
    if not is_valid_date(year, month, day):
        raise Exception("Invalid date.");
    c = year // 100;
    y = year % 100;
    # Break the year code into CCYY
    index = 0;
    index += century_offset[c%4];
    if (c%4 == 0):
        index += (y+3)//4;
    else:
        if y:
            index += (y-1)//4;
    index += y;
    index += month_offset[month];
    if (is_leap_year(year) and month >= 3):
        index += 1;
    index += day;
    return day_index[index%7];
