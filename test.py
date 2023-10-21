from datetime import date

print(date.today())
print(type(date.today()))
# from random import randint
# 31 day long: 01, 03, 05, 07, 08, 10, 12
# 30 day long: 04, 06, 09, 11
year = 2022
year2 = date.today().year
month = date.today().month - 1
day = date.today().day - 1
month_in_days = 0


def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


print(age(date(2003, 1, 17)))


"""
def is_minor(birth_year: int, birth_month: int, birth_day: int):

    year = date.today().year
    month_in_days = 0
    month = date.today().month - 1
    day = date.today().day
    birth_month_in_days = 0

    while year > birth_year:
        leap_year = False
        if year % 4 == 0:
            leap_year = True

        if (birth_month == 1 or birth_month == 3 or birth_month == 5 or
                birth_month == 7 or birth_month == 8 or birth_month == 10 or birth_month == 12):
            birth_month_in_days += 31

        if birth_month == 2 and leap_year:
            birth_month_in_days += 29

        if birth_month == 2 and not leap_year:
            birth_month_in_days += 28

        if birth_month == 4 or birth_month == 6 or birth_month == 9 or birth_month == 11:
            birth_month_in_days += 30

        birth_month -= 1
        if birth_month == 0:
            birth_month = 12
            year -= 1
        if year == birth_year and month == birth_month:
            break

    birth_month_in_days += birth_day

    print(birth_month_in_days)


is_minor(2003, 1, 17)


while year <= year2:

    if year == year2 and month == date.today().month:
        break

    print(year2)
    print(month)
    print(month_in_days)

    leap_year = False

    if year2 % 4 == 0:
        leap_year = True

    if (month == 1 or month == 3 or month == 5 or
            month == 7 or month == 8 or month == 10 or month == 12):
        month_in_days += 31

    if month == 2 and leap_year:
        month_in_days += 29

    if month == 2 and not leap_year:
        month_in_days += 28

    if month == 4 or month == 6 or month == 9 or month == 11:
        month_in_days += 30

    month -= 1

    if month == 0:
        year2 -= 1
        month = 12
        day = 31
    else:
        continue

    if year2 == year and month == date.today().month:
        if (month == 1 or month == 3 or month == 5 or
                month == 7 or month == 8 or month == 10 or month == 12):
            a_day = 31 - day

        if month == 4 or month == 6 or month == 9 or month == 11:
            a_day = 30 - day

        if month == 2 and leap_year:
            a_day = 29 - day
        elif month == 2 and not leap_year:
            a_day = 28 - day



print(month_in_days + day)

a_year = 2023
a_month = randint(1, 9)
a_day = randint(1, 12)
a_month_in_days = 0
year = date.today().year
month = date.today().month
day = date.today().day

while a_month > 0:
    leap_year = False
    if a_year % 4 == 0:
        leap_year = True
    else:
        continue
    if (a_month == 1 or a_month == 3 or a_month == 5 or
            a_month == 7 or a_month == 8 or a_month == 10 or a_month == 12):
        a_month_in_days += 31

    if a_month == 2 and leap_year:
        a_month_in_days += 29

    if a_month == 2 and not leap_year:
        a_month_in_days += 28

    if a_month == 4 or a_month == 6 or a_month == 9 or a_month == 11:
        a_month_in_days += 30

    a_month -= 1
    if a_month == 0:
        a_month = 12
        a_year -= 1
    if year == a_year and month == a_month:
        break

    a_month_in_days += a_day

    print(a_month_in_days)
"""
