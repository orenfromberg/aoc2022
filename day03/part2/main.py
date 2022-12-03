total = 0
with open('./day03/part2/data.txt') as f:
    lines = f.readlines()
    for n in range(0,len(lines),3):
        first = [x for x in lines[n] if x in lines[n+1]]
        second = [x for x in lines[n+1] if x in lines[n+2]]
        both = [x for x in first if x in second][0]
        val = ord(both) - ord('a') + 1 if both.islower() else ord(both) - ord('A')  + 27
        total += val
    print(total)
