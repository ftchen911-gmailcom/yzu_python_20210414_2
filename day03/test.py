
# x + y = 83
# 2x + 4y = 240
x = 1
y = 0
while y <= 60:
    while x <= 83:
        if 2*x + 4*y == 240:
            print(x, y)
        else:
            x = x + 1
            print("2x+4*y=" + str(2*x+4*y))
            print("x=" + str(x))
            print("y.1=" + str(y))
    y = y + 1
    print("y.2=" + str(y))

