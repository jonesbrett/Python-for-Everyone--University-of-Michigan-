import urllib.request, urllib.parse, urllib.error

URL = input("Please enter a website: ")
if len(URL) < 1:
    URL = "http://data.pr4e.org/romeo.txt"

fhand = urllib.request.urlopen(URL)
for line in fhand:
    print(line.decode().strip())
