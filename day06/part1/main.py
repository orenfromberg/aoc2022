with open('./day06/data.txt') as f:
    for line in f:
        for i in range(0,len(line)-4+1):
            test = line[i:i+4]
            if(len(set([x for x in test])) == 4):
                print(i+4)
                break
