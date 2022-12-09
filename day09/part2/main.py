import math

# rope = [(0,0),(0,0)]
rope = []
for i in range(10):
    rope.append((0,0))
stack = []

def add(x : tuple,y : tuple):
    return tuple(x + y for x,y in zip(x, y))

def subtract(x : tuple,y : tuple):
    return tuple(x - y for x,y in zip(x, y))

def distance(x: tuple, y: tuple):
    diff = subtract(x, y)
    return math.sqrt(diff[0]*diff[0] + diff[1]*diff[1])

def move(direction: str):
    global rope
    global stack

    head = rope[0]

    if (direction == 'R'):
        head = add(head, (1, 0))
    elif (direction == 'L'):
        head = add(head, (-1, 0))
    elif (direction == 'U'):
        head = add(head, (0, 1))
    elif (direction == 'D'):
        head = add(head, (0, -1))

    rope[0] = head

    # process tail
    for i in range(len(rope)-1):
        head = rope[i]
        tail = rope[i+1]

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
        rope[i+1] = tail
    # push tail loc
    stack.append(rope[len(rope)-1])


with open('./day09/data.txt') as f:
    for line in f:
        direction, count = line.strip().split(' ')
        for i in range(int(count)):
            move(direction)

print(len(set(stack)))