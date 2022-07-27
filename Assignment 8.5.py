fname = input("Enter file name: ")
fh = open(fname)
count = 0
# if len(fname) < 1:
# fname = "mbox-short.txt"
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue

    else:
        word = line.split()
        print(word[1])
        count = count + 1


print("There were", count, "lines in the file with From as the first word")
