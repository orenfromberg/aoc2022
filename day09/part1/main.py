import math

head = (0,0)
tail = (0,0)
tail_locations = []

def add(x : tuple,y : tuple):
    return tuple(x + y for x,y in zip(x, y))

def subtract(x : tuple,y : tuple):
    return tuple(x - y for x,y in zip(x, y))

def distance(x: tuple, y: tuple):
    diff = subtract(x, y)
    return math.sqrt(diff[0]*diff[0] + diff[1]*diff[1])

def move(direction: str):
    global head
    global tail
    global tail_locations

    if (direction == 'R'):
        head = add(head, (1, 0))
    elif (direction == 'L'):
        head = add(head, (-1, 0))
    elif (direction == 'U'):
        head = add(head, (0, 1))
    elif (direction == 'D'):
        head = add(head, (0, -1))

    d = distance(head, tail)
    diff = subtract(head, tail)
    if (d == 2):
        tail = add(tail, (diff[0]*.5,diff[1]*.5))
    elif (d > math.sqrt(2)):
        diff = subtract(head,tail)
        if(diff[0] > 0 and diff[1] > 0):
            tail = add(tail, (1,1))
        elif(diff[0] > 0 and diff[1] < 0):
            tail = add(tail, (1,-1))
        elif(diff[0] < 0 and diff[1] < 0):
            tail = add(tail, (-1,-1))
        elif(diff[0] < 0 and diff[1] > 0):
            tail = add(tail, (-1,1))
        
    # push tail loc
    tail_locations.append(tail)


with open('./day09/data.txt') as f:
    for line in f:
        direction, count = line.strip().split(' ')
        for i in range(int(count)):
            move(direction)

print(len(set(tail_locations)))