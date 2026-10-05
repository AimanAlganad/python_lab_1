import os
import time
GREEN = "\u001b[42m"
RESET = "\u001b[0m"
YELLOW = "\u001b[43m"
RED = "\u001b[41m"
for i in range(3):
    print(GREEN + ' ' * 8 + YELLOW + ' ' * 12 + RESET)
for i in range(3):
    print(GREEN + ' ' * 8 + RED + ' ' * 12 + RESET)
print()
# Task 2: Pattern h
def draw_pattern():
    height = 15
    center = height // 2
    offset = height // 2
    step = 1
    length = 1
    distance = 10

    for line in range(height):
        if length < distance:
            print(
                ' ' * offset
                + GREEN + ' ' * length + RESET
                + ' ' * (distance - length)
                + GREEN + ' ' * length + RESET
            )
        else:
            print(
                ' ' * offset
                + GREEN + ' ' * (length + distance) + RESET
            )

        if line < center:
            offset -= step
            length += step * 2
        else:
            offset += step
            length -= step * 2


draw_pattern()
print()
# Task 3: Animation
input("Нажмите Enter, чтобы начать анимацию...")

def animate():
    column = 1

    for frame in range(4):
        os.system("cls")

        for row in range(3, 6):
            print(
                "\u001b[" + str(row) + ";" + str(column) + "H"
                + GREEN + ' ' * 6 + RESET
            )

        time.sleep(0.3)
        column += 8

animate()

print()
# Task 4: Sequence.txt
def sequence():
    file = open("sequence.txt", "r")
    positive = []
    negative = []
    
    for line in file:
        number = float(line)
        if 0<= number <=5:
            positive.append(number)
        elif -5<= number < 0:
            negative.append(number)
    
    file.close()
    
    positive_count = len(positive)
    negative_count = len(negative)
    total = positive_count + negative_count

    positive_percent = positive_count / total * 100
    negative_percent = negative_count / total * 100
    total = positive_count + negative_count

    positive_length = int(positive_percent / 2)
    negative_length = int(negative_percent / 2)

    print(GREEN + " " * positive_length + RESET, f"{positive_percent:.1f}%")
    print(RED + " " * negative_length + RESET, f"{negative_percent:.1f}%")

sequence()