# This code calculates how many days exist between two
# dates, and accounts for leap days. Input must be:
# daysBetweenDates( year1, month1, day1, year2, month2, day2 )
# with the later date being entered later

# daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# leap year algorithm found on:
# https://en.wikipedia.org/wiki/Leap_year#Algorithm

# Returns Boolean value whether input is leap year or not
def leapyear(yr):
    rem1 = yr/4.0
    rem2 = yr/100.0
    rem3 = yr/400.0
    if str(rem1)[-1] != '0':
        leap = False
    else:
        if str(rem2)[-1] != '0':
            leap = True
        else:
            if str(rem3)[-1] != '0':
                leap = False
            else: leap = True
    return leap

# Returns number of days in a month given month and year
def daysinmonth(mon,bb):
    monthvalue = 0
    if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
        monthvalue = 31
    if mon == 4 or mon == 6 or mon == 9 or mon == 11:
        monthvalue = 30
    if mon == 2:
        if leapyear(bb) == True:
            monthvalue = 29
        else:
            monthvalue = 28
    return monthvalue

# Returns number of days in a given year
def daysinyear(aa):
    yearvalue = 0
    leap = leapyear(aa)
    if leap == True:
        yearvalue = 366
    else: yearvalue = 365
    return yearvalue

# Returns number of days between two dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    currentyear = year1
    currentmonth = month1
    currentday = day1
    
    while currentday != day2:
        days = days + 1
        currentday = currentday + 1
        if currentday > daysinmonth(currentmonth,currentyear):
            currentmonth = currentmonth + 1
            currentday = 1
    
    while currentyear < year2-1:
        days = days + daysinyear(currentyear)
        currentyear = currentyear + 1
        if currentyear == year2-1: break
        
    while currentyear != year2:    
        days = days + daysinmonth(currentmonth,currentyear)
        currentmonth = currentmonth + 1
        if currentmonth > 12:
            currentmonth = 1
            currentyear = currentyear + 1
    
    while currentyear == year2:
        while currentmonth < month2:
            days = days + daysinmonth(currentmonth,currentyear)
            currentmonth = currentmonth + 1
        break
                
    return days
 
        
print daysBetweenDates(2011,1,1,2012,8,8)
print daysinmonth(2,2012)
print leapyear(2012)
print str(2012/4.0)[-1]
print str(2012/100.0)[-1]
print str(2012/400.0)[-1]

# Test routine

#def test():
#    test_cases = [((2012,1,1,2012,2,28), 58), 
#                  ((2012,1,1,2012,3,1), 60),
#                  ((2011,6,30,2012,6,30), 366),
#                  ((2011,1,1,2012,8,8), 585 ),
#                  ((1900,1,1,1999,12,31), 36523)]

