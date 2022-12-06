# stacks = [[x for x in 'ZN'], [x for x in 'MCD'], [x for x in 'P']]
stacks = [
    [x for x in 'RSLFQ'],
    [x for x in 'NZQGPT'],
    [x for x in 'SMQB'],
    [x for x in 'TGZJHCBQ'],
    [x for x in 'PHMBNFS'],
    [x for x in 'PCQNSLVG'],
    [x for x in 'WCF'],
    [x for x in 'QHGZWVPM'],
    [x for x in 'GZDLCNR'],
    ]

with open('./day05/data.txt') as f:
    for line in f:
        a = line.strip().split(' ')
        num = int(a[1])
        s_from = int(a[3]) - 1
        s_to = int(a[5]) - 1
        temp = []
        for i in range(num):
            foo = stacks[s_from].pop()
            temp.append(foo)
        for i in range(len(temp)):
            stacks[s_to].append(temp.pop())
result = ''
for i in range(len(stacks)):
    result += stacks[i].pop()
print(result)