year = int(input("What year is it? : "))


if year % 100 == 0:
    year = year / 400
    if year.is_integer():
        print("This year is a centennial/centurial leap year!")
    else:
        print("This year is not a centennial/centurial leap year.")
else:
    year = year / 4
    if year.is_integer():
        print("This year is a leap year!")
    else:
        print("This year is not a leap year.")
