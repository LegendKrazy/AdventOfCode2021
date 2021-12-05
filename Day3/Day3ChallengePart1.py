from collections import Counter

# Advent of Code 2021 Day 3 Part 1 Use the binary numbers in the diagnostic report to generate two new binary numbers
# (gamma rate and epsilon rate). Power consumption = gamma rate * epsilon rate. Each bit in the gamma rate can be
# determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
binarylist = []
with open("Day3Input.txt") as file:
    while line := file.readline().rstrip():
        binarylist.append(line)


def rate(binarylist):
    singledigits = []
    gammaresult = ""
    epsilonresult = ""
    for c in range(12):
        for i in binarylist:
            singledigits.append(i[c])
        mostoccurences = Counter(singledigits)
        mostfreq = mostoccurences.most_common(1)
        leastfreq = mostoccurences.most_common(2)
        gammaresult += mostfreq[0][0]
        epsilonresult += leastfreq[1][0]
        singledigits = []

    gammaresult = int(gammaresult, 2)
    epsilonresult = int(epsilonresult, 2)
    print("Answer is: ", (gammaresult * epsilonresult))


rate(binarylist)
