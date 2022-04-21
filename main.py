import re
from datetime import datetime
import os

folder = "Data"
files = os.listdir(folder)

output = open("result.csv", "w", encoding="utf-8")

output.write("ID, condition, human, computer, moves, time\n")

for file in files:
    f = open(os.path.join(folder, file), encoding="utf-8")
    content = f.readlines()
    f.close()

    for line in content:
        line = line.strip()
        tokens = re.split(", ", line)
        if tokens != [""]:
            answer = tokens[0].split(" ")
            time_start = re.split("]", tokens[1], 2)[0][1:]
            time_start = datetime.strptime(time_start, '%m/%d/%Y %I:%M:%S %p')
            time_end = re.split("]", tokens[-1], 2)[0][1:]
            time_end = datetime.strptime(time_end, '%m/%d/%Y %I:%M:%S %p')
            time_elapsed = time_end - time_start
            output.write(f'{file}, {answer[0]}, {answer[2]}, {answer[5]}, {len(tokens) - 1}, {time_elapsed}\n')

output.close()