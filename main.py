innum = int(input("Enter a number to check if it's positive: "))
if (innum >= 0):
    if (innum > 0):
        print(innum, "is positive.")
    else:
        print(innum, " is neither a positive nor a negative number.")
else:
    print(innum, "is negative")