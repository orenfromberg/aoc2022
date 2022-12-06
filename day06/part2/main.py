n = 14
with open('./day06/data.txt') as f:
    for line in f:
        print([i for i in range(n,len(line)+1) if(len(set([x for x in line[i-n:i]])) == n)][0])