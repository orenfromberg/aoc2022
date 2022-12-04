total = 0
with open('./day03/part2/data.txt') as f:
    lines = f.readlines()
    for n in range(0,len(lines),3):
        badge = [x for x in [x for x in lines[n] if x in lines[n+1]] if x in lines[n+2]][0]
        total += ord(badge) - ord('a') + 1 if badge.islower() else ord(badge) - ord('A') + 27
    print(total)
