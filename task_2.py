'''A function to output date diference in days. Date format being YYYY-MM-DD'''
import datetime

def dates_difference():
    date_format = "%Y-%m-%d"
    firstdate = (input('enter 1st date in this format(y-m-d): '))
    first = datetime.datetime.strptime(firstdate, date_format)
    seconddate = (input('enter 2nd date in this format(y-m-d): '))
    second = datetime.datetime.strptime(seconddate, date_format)
    dates_difference = (second - first).days
    return dates_difference


print(f'Days diferences is: {dates_difference()}days')


