text = "X-DSPAM-Confidence:    0.8475"
start = text.find(":")
# print(start)
number = float(text[start + 1 :].lstrip())
print(number)
