# Advent of Code 2021 Day 2 Part 2 Challenge
# 3rd value added, aim which starts at 0.
# down X increases your aim by X units. up X decreases your aim by X units. forward X does two things:
# It increases your horizontal position by X units and increases your depth by your aim multiplied by X.

commands = ['forward', 'up', 'down']
depth = 0
x_position = 0
aim = 0

with open("Day2Input.txt") as file:
    while line := file.readline().rstrip():
        moveamount = [int(s) for s in line.split() if s.isdigit()]
        for i in commands:
            if i in line:
                # Command match found, make changes accordingly.
                if i == "forward":
                    x_position += moveamount[0]
                    if aim > 0:
                        # Depth changes by horizontal movement * aim
                        depth += (moveamount[0] * aim)
                elif i == "down":
                    aim += moveamount[0]
                elif i == "up":
                    aim -= moveamount[0]
        moveamount = []

result = x_position * depth
print(f'Answer is {result}')
