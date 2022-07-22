# Use the file name mbox-short.txt as the file name
lcount = 0
asc = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    lcount = lcount + 1
    start = line.find(":")
    number = float(line[start + 1 :].lstrip())
    # print(number)
    asc = asc + number

print("Average spam confidence: ", (asc / lcount))
