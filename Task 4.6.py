hrs = input("Enter Hours:")
rate = input("Enter Rate per Hours:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please enter numeric input")
    quit()


def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return (((h - 40) * 1.5) + 40) * r


p = computepay(h, r)
print("Pay", p)

