# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
frs = fr.rstrip()
print(frs.upper())
