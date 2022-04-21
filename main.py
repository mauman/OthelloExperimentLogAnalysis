import re
from datetime import datetime
import os

folder = "Data"
files = os.listdir(folder)

output = open("result.csv", "w", encoding="utf-8")

output.write("ID, condition_code, condition_readable, rated_human, rated_computer, rated_correct, moves, time\n")

for file in files:
    f = open(os.path.join(folder, file), encoding="utf-8")
    content = f.readlines()
    f.close()

    for line in content:
        line = line.strip()
        tokens = re.split(", ", line)
        if tokens != [""]:
            answer = tokens[0].split(" ")
            condition = answer[0][:-1]
            human_readable = ""
            if condition[0] == "W":
                human_readable += "white human wins against "
            else:
                human_readable += "black human wins against "
            if condition[-1] == "H":
                human_readable += "a human"
            else:
                human_readable += "Olivaw"
            rated_human = int(answer[2][:-1])
            rated_computer = int(answer[5][:-1])
            if (condition[-1] == "H" and rated_human > rated_computer) \
            or (condition[-1] == "O" and rated_computer > rated_human):
                rated_correct = "yes"
            elif (condition[-1] == "O" and rated_human > rated_computer) \
            or (condition[-1] == "H" and rated_computer > rated_human):
                rated_correct = "no"
            else:
                rated_correct = "n/a"
            time_start = re.split("]", tokens[1], 2)[0][1:]
            time_start = datetime.strptime(time_start, '%m/%d/%Y %I:%M:%S %p')
            time_end = re.split("]", tokens[-1], 2)[0][1:]
            time_end = datetime.strptime(time_end, '%m/%d/%Y %I:%M:%S %p')
            time_elapsed = time_end - time_start
            output.write(f'{file}, {condition}, {human_readable}, {rated_human}, {rated_computer}, {rated_correct}, {len(tokens) - 1}, {time_elapsed}\n')

output.close()