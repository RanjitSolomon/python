import math

def paint_calc(height, width, cover):
    print(f" paint {math.ceil((height * width) / cover) }")


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


