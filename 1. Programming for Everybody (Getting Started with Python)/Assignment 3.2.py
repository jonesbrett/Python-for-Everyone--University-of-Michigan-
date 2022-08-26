import string


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hours:")
r = rate
try:
    if h <= 40:
        print(h * float(r))
    else:
        print((((h - 40) * 1.5) + 40) * float(r))

except:
    print("Please enter numeric input")
