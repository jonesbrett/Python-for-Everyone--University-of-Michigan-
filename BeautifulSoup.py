import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

URL = input("Please enter a website: ")
if len(URL) < 1:
    URL = "http://www.dr-chuck.com/page1.htm"

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
