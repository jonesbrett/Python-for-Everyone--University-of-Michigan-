import re

hand = open("regex_sum_42.txt")
total = 0
count = 0
for line in hand:
    # count = count + 1
    line = line.rstrip()

    x = re.findall("[0-9]+", line)

    for i in x:
        total += int(i)

print(total)
