# Advent of Code 2021 Day 2 Challenge part 1
# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Your horizontal position and depth both start at 0
# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?
commands = ['forward', 'up', 'down']
depth = 0
x_position = 0

with open("Day2Input.txt") as file:
    while line := file.readline().rstrip():
        moveamount = [int(s) for s in line.split() if s.isdigit()]
        for i in commands:
            if i in line:
                # Command match found, make changes accordingly.
                if i == "forward":
                    x_position += moveamount[0]
                elif i == "down":
                    depth += moveamount[0]
                elif i == "up":
                    depth -= moveamount[0]
        moveamount = []

result = x_position * depth
print(f'Answer is {result}')
