from datetime import date
from random import randint
from size import sample
from time import time

start = time()
sample_size = sample()

birth_dates_list = []


def birth_dates():

    # dates of birth
    this_year = date.today().year
    this_month = date.today().month
    this_day = date.today().day

    # years
    for j in range(sample_size):
        birth_year = randint(1910, this_year)
        birth_dates_list.append([birth_year])

    # months
    for j in range(sample_size):
        if birth_dates_list[j] == this_year:
            birth_dates_list[j].append(randint(1, this_month))
        else:
            birth_dates_list[j].append(randint(1, 12))

    # 31 day long: 01, 03, 05, 07, 08, 10, 12
    # 30 day long: 04, 06, 09, 11

    # days
    for j in range(sample_size):
        if birth_dates_list[j][0] == this_year and birth_dates_list[j][1] == this_month:

            birth_dates_list.append(randint(1, this_day))
        else:

            if birth_dates_list[j][1] == 2 and birth_dates_list[j][0] % 4 == 0:

                birth_dates_list[j].append(randint(1, 29))
            else:

                if int(birth_dates_list[j][0]) % 4 != 0 and birth_dates_list[j][1] == 2:

                    birth_dates_list[j].append(randint(1, 28))
                else:
                    # birth_dates_list[j][1] != 2 and
                    if (birth_dates_list[j][1] == 1 or birth_dates_list[j][1] == 3 or birth_dates_list[j][1] == 5 or

                            birth_dates_list[j][1] == 7 or birth_dates_list[j][1] == 8 or

                            birth_dates_list[j][1] == 10 or birth_dates_list[j][1] == 12):

                        birth_dates_list[j].append(randint(1, 31))
                    else:
                        if (birth_dates_list[j][1] == 4 or birth_dates_list[j][1] == 6 or birth_dates_list[j][1] == 9 or

                                birth_dates_list[j][1] == 11):

                            birth_dates_list[j].append(randint(1, 30))

    if len(birth_dates_list) == sample_size:
        for j in range(len(birth_dates_list)):
            birth_dates_list[j][0] = str(birth_dates_list[j][0])
            birth_dates_list[j][1] = str(birth_dates_list[j][1])
            birth_dates_list[j][2] = str(birth_dates_list[j][2])

        output = open("birth_dates.txt", "w", encoding="utf-8")

        for i in birth_dates_list:
            print(".".join(i), file=output)

        output.close()


birth_dates()


def p_time2(end):
    return print(f"date_of_births: {end - start}")


p_time2(time())
