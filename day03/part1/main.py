def get_priority(line):
    item1, item2 = line[:len(line)//2], line[len(line)//2:]
    both = [x for x in item1 if x in item2][0]
    val = ord(both) - ord('a') + 1 if both.islower() else ord(both) - ord('A')  + 27
    return val

total = 0
with open('./day03/part1/data.txt') as f:
    for line in f:
        total += get_priority(line.strip())

print(total)