text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
# print(start)
finish = text.find("5")
# print(finish)
number = float(text[start : finish + 1])
print(number)
