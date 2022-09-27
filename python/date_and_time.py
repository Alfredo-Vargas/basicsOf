from datetime import datetime

# Syntax datetime
# From left to right:
# year, month, day, hours, minutes, seconds, microseconds
# 2021-09-11 21:24:09.250666

# Character codes for formatting datetime values:
# %a first three characters of the weekday, e.g. Wed
# %A full name of the weekday, e.g. Wednesday
# %b first three characters of the month, e.g. Apr
# %B full name of the month, e.g. April
# %d day of the month as a zero-padded number (01-31)
# %w weekday as a number (0 – 6), with Sunday being 0
# %m month as a zero-padded number (01 – 12)
# %y year in two-digit format, e.g. "21" instead of "2021"
# %H hours (24h notation) as zero-padded number (00-23)
# %I hours (12h notation) as zero-padded number (00-11)
# %M minutes as zero-padded number (00-59)
# %S seconds as zero-padded number (00-59)
# %f microseconds (000000 – 999999)
# %p AM/PM for time
# %Z the timezone
# %z UTC offset



def main() -> None:
    x = datetime(2021, 9, 16, 11, 51, 36)
    print(type(x))
    print(x)

    # datetime substraction
    date1 = datetime.now()
    date2 = datetime(2021, 9, 20)
    diff = date2 - date1
    print(type(diff))
    print(diff)

    # convert datetime to readable string using "strtime"
    print(x.strftime("%b %d %Y %H:%M:%S"))

    # creating datetime from string using "strptime"
    s = '9/16/21'
    y = datetime.strptime(s, '%m/%d/%y')
    print(y)

if __name__ == "__main__":
    main()
