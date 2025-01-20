import random


def drawDice(num):
    match num:
        case 1:
            print("""
            |-------------|
            |             |
            |      O      |
            |             |
            |-------------|
            """, end="")
        case 2:
            print("""
            |-------------|
            |  O          |
            |             |
            |          O  |
            |-------------|
            """, end="")
        case 3:
            print("""
            |-------------|
            |  O          |
            |      O      |
            |          O  |
            |-------------|
            """, end="")
        case 4:
            print("""
            |-------------|
            |  O       O  |
            |             |
            |  O       O  |
            |-------------|
            """, end="")
        case 5:
            print("""
            |-------------|
            |  O       O  |
            |      O      |
            |  O       O  |
            |-------------|
            """, end="")
        case 6:
            print("""
            |-------------|
            |  O       O  |
            |  O       O  |
            |  O       O  |
            |-------------|
            """, end="")
        case _:
            raise ValueError


options = {i for i in range(2, 13)}
a = random.randint(1, 6)
b = random.randint(1, 6)
c = a + b

running = True
while running:
    if (not options) or (a not in options and b not in options and c not in options):
        print("Player Won")
        running = False
    drawDice(a)
    drawDice(b)
    print(f"\nOptions: {options}")
    playersPick = int(input(f"Which number to use? 1:({a} and {b}) 2:{c} 3: Give up."))
    if playersPick == 1:
        if a in options and b in options:
            options.remove(a)
            options.remove(b)
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            c = a + b
        else:
            print("Try again.")
    elif playersPick == 2:
        if c in options:
            options.remove(c)
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            c = a + b
    elif playersPick == 3:
        running = False
