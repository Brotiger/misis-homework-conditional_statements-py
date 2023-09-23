x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

h11 = ((x2 - x1 == 2) or (x1 - x2 == 2)) and ((y2 - y1 == 1) or (y1 - y2 == 1))
h12 = ((x2 - x1 == 1) or (x1 - x2 == 1)) and ((y2 - y1 == 2) or (y1 - y2 == 2))
h21 = ((x1 - x2 == 2) or (x2 - x1 == 2)) and ((y1 - y2 == 1) or (y2 - y1 == 1))
h22 = ((x1 - x2 == 1) or (x2 - x1 == 1)) and ((y1 - y2 == 2) or (y2 - y1 == 2))

r11 = x1 == x2 and y1 != y2
r21 = x1 != x2 and y1 == y2

e = x1 != x2 and y1 != y2
e11 = x1 == y1 and x2 == y2 and e
e21 = x1 == y2 and x2 == y1 and e

if r11 or r21:
    print("Ладья может совершить такой ход")
else:
    print("Ладья не может совершить такой ход")

if e11 or e21:
    print("Слон может совершить такой ход")
else:
    print("Слон не может совершить такой ход")

if h11 or h12 or h21 or h22:
    print("Конь может совершить такой ход")
else:
    print("Конь не может совершить такой ход")