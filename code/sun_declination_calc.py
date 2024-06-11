# ***********************************************************
# ** calculate the declination of the sun at a given time  **
# ** using two different methods:                          **
# ** 1. more accurate calculation using the formula        **
# **    provided in the book "Astronomical Algorithms"     **
# ** 2. a simpler approximation method                     **
# **                                                       **
# ** rev 1 - shabaz - june 2024                            **
# ***********************************************************

import math

# ******** get system current date/month/year ********
import datetime
now = datetime.datetime.now()
date = now.day
month = now.month
year = now.year

# ******** constants ***********
PI = 3.141592654
RAD = PI / 180.0  # radians per degree (some of the calculations require angles in radians)
JULIAN_CENTURY = 36525.0  # number of days per 100 years
YEAR_1900_JD = 2415020.0  # julian day for 1st January 1900

# function to calculate the julian day
# (number of days since 1st January in the year 4713 BC)
def julian_date(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year // 100
    b = 2 - a + a // 4
    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5
    return jd + 0.5  # add 0.5 to get the julian day at noon UTC

# calculate the declination of the sun
def sun_declination(jd):
    t0 = (jd - YEAR_1900_JD) / JULIAN_CENTURY  # number of centuries since the year 1900, this will be approx. 1.244 in 2024
    M = 358.47583 + 35999.04975 * t0 - 0.000150 * t0 * t0 - 0.0000033 * t0 * t0 * t0  # mean anomaly
    M = M % 360
    Lsun = 279.69668 + 36000.76892 * t0 + 0.0003025 * t0 * t0  # mean longitude of the sun
    Lsun = Lsun % 360
    Cen = (1.919460 - 0.004789 * t0 - 0.000014 * t0 * t0) * math.sin(M*RAD) + (0.020094 - 0.000100 * t0) * math.sin(2 * M*RAD) + 0.000293 * math.sin(3 * M*RAD)  # sun's equation of center
    Stheta = Lsun + Cen  # apparent longitude of the sun
    Stheta = Stheta % 360
    omeg = 259.18 - 1934.142 * t0  # longitude of the ascending node of the moon
    thapp = Stheta - 0.00569 - 0.00479 * math.sin(omeg*RAD)  # apparent sidereal time
    epli = 23.452294 - 0.0130125 * t0 - 0.00000164 * t0 * t0 + 0.000000503 * t0 * t0 * t0 + 0.00256 * math.cos(omeg*RAD)  # obliquity of the ecliptic
    DEC = math.asin(math.sin(epli*RAD) * math.sin(thapp*RAD))/RAD  # declination of the sun
    return DEC

def sun_declination_simple(date, month, year):
    # first calculate the day of the year
    day_of_year = 0
    for i in range(1, month):
        if i == 2:
            # check for leap year
            if year % 4 == 0:
                day_of_year += 29
            else:
                day_of_year += 28
        elif i in [4, 6, 9, 11]:
            day_of_year += 30
        else:
            day_of_year += 31
    day_of_year += date
    declination = -23.44 * math.cos((360.0/365.0) * (day_of_year + 9)*RAD)  # declination of the sun
    return declination


jd = julian_date(year, month, date)  # julian day at noon UTC
print(f"Julian day for DD:MM:YYYY {date}:{month}:{year} at noon UTC is: {jd:.0f}")

declination = sun_declination(jd)  # this is the more accurate calculation
print(f"Declination of the sun is: {declination:.3f}")

simple_declination = sun_declination_simple(date, month, year)
print(f"Simpler approximation method result is: {simple_declination:.3f}")

