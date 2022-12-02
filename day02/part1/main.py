def compute_score(line):
    s = line.split()
    score = 0

    match s:
        # lose
        case ['A', 'Z']:
            score += 0 + 3
        case ['B', 'X']:
            score += 0 + 1
        case ['C', 'Y']:
            score += 0 + 2
        # draw
        case ['A', 'X']:
            score += 3 + 1
        case ['B', 'Y']:
            score += 3 + 2
        case ['C', 'Z']:
            score += 3 + 3
        # win
        case ['A', 'Y']:
            score += 6 + 2
        case ['B', 'Z']:
            score += 6 + 3
        case ['C', 'X']:
            score += 6 + 1
    return score

total = 0
with open('./day02/part1/data.txt') as f:
    for line in f:
        total += compute_score(line)

print(total)