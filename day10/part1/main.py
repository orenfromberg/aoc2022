def cycle():
    global instruction
    global values
    global cycle_count
    global x

    cycle_count += 1
    instruction[1] -= 1
    if(instruction[1] == 0):
        x += instruction[0]

    values.append(x)

x = 1
instruction = [] # [addend, count]
values = [1]
cycle_count = 0
with open('./day10/data.txt') as f:
    for line in f:
        i = line.strip()
        if(i[:4] == 'addx'):
            _, p = i.split(' ')
            instruction = [int(p), 2]
            for i in range(2):
                cycle()
        elif(i[:4] == 'noop'):
            instruction = [0, 1]
            cycle()

print(sum([values[i]*(i+1) for i in range(20-1,220,40)]))