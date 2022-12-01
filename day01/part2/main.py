sum = 0
sums = []
with open('./data.txt') as f:
    for line in f:
        if (line != "\n"):
            sum += int(line)
        else:
            sums.append(sum)
            sum = 0
            continue
    if sum > 0:
        sums.append(sum)

sums.sort(reverse=True)

sum = 0
for x in range(3):
    sum += sums[x]

print(sum)