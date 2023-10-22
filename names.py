from threading import Thread
from random import randint
from size import sample
from time import time

start = time()
sample_size = sample()

surnames = []
female_first_names = []
male_first_names = []
made_up_names = []


def names():

    def surnames_():
        a = open("names.txt", encoding="utf-8")
        for row in a:
            row = row.strip()
            data_row = row.split(" ")
            surnames.append(data_row[0])

    def female_first_names_():
        b = open("female first names.txt", encoding="utf-8")
        for row in b:
            row = row.strip()
            data_row = row.split(" ")
            female_first_names.append(data_row[0])

    def male_first_names_():
        c = open("male first names.txt", encoding="utf-8")
        for row in c:
            row = row.strip()
            data_row = row.split(" ")
            male_first_names.append(data_row[0])

    t1 = Thread(surnames_())
    t2 = Thread(female_first_names_())
    t3 = Thread(male_first_names_())

    t1.start()
    t2.start()
    t3.start()

    # 2 = female, 1 = male
    gender = randint(1, 2)
    duo_first_names = randint(1, 2)

    def p5():
        while len(made_up_names) < sample_size:
            temp = []

            if gender == 2:

                if duo_first_names == 1:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])

    # 2 female 1st names
                else:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])
            else:
                if gender == 1:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])
                else:

                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])

    def p6():
        while len(made_up_names) < sample_size:
            temp = []

            if gender == 2:

                if duo_first_names == 1:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])

    # 2 female 1st names different thread
                else:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_first_name = female_first_names[randint(0, len(female_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])
            else:
                if gender == 1:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])
                else:
                    rnd_surname = surnames[randint(0, len(surnames) - 1)]
                    temp.append(rnd_surname)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_first_name = male_first_names[randint(0, len(male_first_names) - 1)]
                    temp.append(rnd_first_name)

                    rnd_name = " ".join(temp)
                    made_up_names.append([rnd_name])

    t5 = Thread(p5())
    t5.start()
    t6 = Thread(p6())
    t6.start()

    output = open("made_up_names.txt", "w", encoding="utf-8")

    for i in made_up_names:
        print(" ".join(i), file=output)

    output.close()


names()


def p_time1(end):
    return print(f"names: {end - start}")


p_time1(time())
