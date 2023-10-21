with open("New Text.txt", encoding="utf-8") as f:
    lines = f.readlines()

    surnames_dic = {}

    for line in lines:
        rank, surnames, num, ratio = line.strip().split("\t")
        surnames_dic[surnames] = int(num), ratio


temp = []
for item in surnames_dic.items():
    temp.append([item[0], item[1]])

minus = int(temp[0][1][1][2:4])
minus_counter = 0
while 1000 % minus != 0:
    minus = int(temp[0][1][1][2:4]) - minus_counter
    minus_counter += 1

plus = int(temp[0][1][1][2:4])
plus_counter = 0
while 1000 % plus != 0:
    plus = int(temp[0][1][1][2:4]) + plus_counter
    plus_counter += 1

if plus_counter > minus_counter:
    minus
else:
    plus
