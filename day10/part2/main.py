import re

def cycle(instruction):
    global values
    global cycle_count
    global x

    col = cycle_count % 40
    print('#' if(x == col or x-1==col or x+1 ==col) else '.',end='\n' if col == 39 else '')

    cycle_count += 1
    instruction[1] -= 1
    if(instruction[1] == 0):
        x += instruction[0]

    values.append(x)

x = 1
instruction = []
values = [1]
cycle_count = 0
with open('./day10/data.txt') as f:
    for line in f:
        i = line.strip()
        if(re.match('addx',i)):
            _, p = i.split(' ')
            instruction = [int(p), 2]
            for i in range(2):
                cycle(instruction)
        elif(re.match('noop',i)):
            instruction = [0, 1]
            cycle(instruction)