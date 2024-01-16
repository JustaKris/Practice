#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract hours, minutes, and seconds
    hh, mm, ss = map(int, s[:-2].split(':'))
    period = s[-2:]

    # Adjust hours for PM and midnight
    if period == 'PM' and hh < 12:
        hh += 12
    elif period == 'AM' and hh == 12:
        hh = 0

    # Convert to 24-hour format and format the result
    result = "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
    return result


if __name__ == '__main__':
    s = input()

    print(timeConversion(s))

""" Test Case 1
07:05:45PM
"""
