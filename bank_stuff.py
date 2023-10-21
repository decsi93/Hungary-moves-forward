from size import sample
from random import randint
from time import time

start = time()
sample_size = sample()


bank_accounts = []
bank_balance = []


def bank__stuf():

    banks = ["Erste", "Raiffaisen", "K&H", "OTP", "Budapest Bank", "CIB"]
    for i in range(sample_size):
        bank_accounts.append([banks[randint(0, len(banks) - 1)]])

    output = open("bank_accounts.txt", "w", encoding="utf-8")

    for i in bank_accounts:
        print("".join(i), file=output)

    output.close()


bank__stuf()


def p_time4(end):
    return print(f"bank_stuff: {end - start}")


p_time4(time())
