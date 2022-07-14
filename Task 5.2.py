largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
        # print(inum)
        if largest is None or inum >= largest:
            largest = inum
            # print("largest is set to", largest)
            continue

        elif smallest is None or inum <= smallest:
            smallest = inum
            # print("smallest is set to", smallest)
            continue

        elif inum < largest or inum > smallest:
            # print("not bigger or smaller")
            continue
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

