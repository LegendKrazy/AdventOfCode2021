# # Advent of Code 2021 Day 1 part 2 Challenge
# Your goal now is to count the number of times the sum of measurements in this sliding window
# increases from the previous sum. So, compare A with B, then compare B with C, then C with D,
# and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

windows = []
largerwindows = 0

with open("Day1Input.txt") as file:
    while line := file.readline().rstrip():
        windows.append(int(line))

for i in range(len(windows)):
    if len(windows) > 3:
        window1 = sum(windows[0:3])
        window2 = sum(windows[1:4])
        if window1 < window2:
            largerwindows += 1
    del windows[:1]

print(f'Windows increased in size {largerwindows} times.')
