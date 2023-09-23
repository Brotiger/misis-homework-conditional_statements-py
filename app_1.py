day = int(input("День: "))
year = int(input("Год: "))

if day == 29 and ((year % 4) == 0 and (year % 100) != 0) or year % 400 == 0:
    print("особо ценный программист")
elif day != 29:
    print("обычный программист")
else:
    print("мошенник")