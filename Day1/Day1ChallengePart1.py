# count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)
# noinspection SpellCheckingInspection
depthlist = []
countincrease = 0

with open("Day1Input.txt") as file:
    while line := file.readline().rstrip():
        depthlist.append(int(line))

for i in range(len(depthlist)):
    if len(depthlist) > 1:
        if depthlist[0] < depthlist[1]:
            countincrease += 1
    depthlist.pop(0)

print(f'Depth increased {countincrease} times.')
