count=0
with open('./day04/part2/data.txt') as f:
    for line in f:
        left, right = line.strip().split(',')
        lmin, lmax = [int(x) for x in left.split('-')]
        rmin, rmax = [int(x) for x in right.split('-')]
        first = set(range(lmin, lmax+1))
        second = set(range(rmin, rmax+1))
        if (first & second):
            count += 1
    print(count)

