with open('./day06/data.txt') as f:
    for line in f:
        for i in range(0,len(line)-14+1):
            test = line[i:i+14]
            if(len(set([x for x in test])) == 14):
                print(i+14)
                break
