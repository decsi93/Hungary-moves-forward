from random import randint
from size import sample
from time import time

start = time()
sample_size = sample()

ID_nums = []
health_insurance_num = []
VAT_IDs = []


def IDs():

    # ID num
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V",
                "W", "X", "Y", "Z"]

    for i in range(sample_size):
        ID_nums.append([str(randint(100_000, 999_999)), alphabet[randint(0, len(alphabet)-1)],
                        alphabet[randint(0, len(alphabet)-1)]])

    output = open("ID_nums.txt", "w", encoding="utf-8")

    for i in ID_nums:
        print("".join(i), file=output)

    output.close()

    # health insurance num
    for i in range(sample_size):
        health_insurance_num.append([str(randint(100_000_000, 999_999_999))])

    output = open("health_insurance_num.txt", "w", encoding="utf-8")

    for i in health_insurance_num:
        print("".join(i), file=output)

    output.close()

    # VAT ID
    for i in range(sample_size):
        VAT_IDs.append(str(randint(100_000_000_000_0, 999_999_999_999_9)))

    output = open("VAT_IDs.txt", "w", encoding="utf-8")

    for i in VAT_IDs:
        print("".join(i), file=output)

    output.close()


IDs()


def p_time3(end):
    return print(f"IDs: {end - start}")


p_time3(time())
