name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senderaddresses = list()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        fromline = line.split()
        sender = fromline[1]
        senderaddresses.append(sender)
        counts = dict()
        for addresses in senderaddresses:
            counts[addresses] = counts.get(addresses, 0) + 1

bigcount = None
bigword = None
for addresses, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = addresses
        bigcount = count

# print(counts)
print(bigword, bigcount)
