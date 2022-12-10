import re

def execute(i):
    global x
    if(re.match('addx',i)):
        _, p = i.split(' ')
        x += int(p)
    elif(re.match('noop',i)):
        x += 0

def cycle(instructions):
    global values
    global cycle_count

    col = cycle_count % 40
    if (x == col or x-1==col or x+1 ==col):
        print('#',end='\n' if col == 39 else '')
    else:
        print('.',end='\n' if col == 39 else '')

    cycle_count += 1

    # decrement counter for all instructions
    for i in instructions:
        i[1] -= 1
        if(i[1] == 0):
            execute(i[0])
    # clean out
    for i in range(len(instructions)):
        if(instructions[i][1] == 0):
            instructions.pop(i)
            break

    values.append(x)


x = 1
instructions = []
values = [1]
cycle_count = 0
with open('./day10/data.txt') as f:
    for line in f:
        i = line.strip()
        if(re.match('addx',i)):
            instructions.append([i,2])
            for i in range(2):
                cycle(instructions)
        elif(re.match('noop',i)):
            instructions.append([i,1])
            cycle(instructions)