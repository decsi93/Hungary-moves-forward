from time import time
from random import randint
from threading import Thread
from size import sample
from names import names
from date_of_births import birth_dates
from IDs import IDs
from bank_stuff import bank__stuf

start = time()

sample_size = sample()

names()
birth_dates()
IDs()
bank__stuf()

made_up_names = []
birth_dates_list = []
ID_nums = []
health_insurance_nums = []
VAT_IDs = []
bank_accounts = []


def made__up__names():
    a = open("made_up_names.txt", encoding="utf-8")
    for row in a:
        row = row.strip()
        data_row = row.split("\n")
        made_up_names.append(data_row[0])
    a.close()


def birth__dates__list():
    b = open("birth_dates.txt", encoding="utf-8")
    for row in b:
        row = row.strip()
        data_row = row.split(" ")
        birth_dates_list.append(data_row[0])
    b.close()


def id__nums():
    c = open("ID_nums.txt", encoding="utf-8")
    for row in c:
        row = row.strip()
        data_row = row.split(" ")
        ID_nums.append(data_row[0])
    c.close()


def health__insurance__nums():
    d = open("health_insurance_num.txt", encoding="utf-8")
    for row in d:
        row = row.strip()
        data_row = row.split(" ")
        health_insurance_nums.append(int(data_row[0]))
    d.close()


def vat__ids():
    e = open("VAT_IDs.txt", encoding="utf-8")
    for row in e:
        row = row.strip()
        data_row = row.split(" ")
        VAT_IDs.append(int(data_row[0]))
    e.close()


def bank__accounts():
    f = open("bank_accounts.txt", encoding="utf-8")
    for row in f:
        row = row.strip()
        data_row = row.split("\n")
        bank_accounts.append(data_row[0])
    f.close()


t1 = Thread(made__up__names())
t2 = Thread(birth__dates__list())
t3 = Thread(id__nums())
t4 = Thread(health__insurance__nums())
t5 = Thread(vat__ids())
t6 = Thread(bank__accounts())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


data_base = []
for i in range(sample_size):
    data_base.append([made_up_names[randint(0, len(made_up_names) - 1)],

                      birth_dates_list[randint(0, len(birth_dates_list) - 1)],

                      ID_nums[randint(0, sample_size - 1)],

                      health_insurance_nums[randint(0, sample_size - 1)],

                      VAT_IDs[randint(0, len(VAT_IDs) - 1)],

                      bank_accounts[randint(0, sample_size - 1)]])

print(f"proof_of_concept: {time() - start}")
