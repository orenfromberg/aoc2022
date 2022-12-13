def get_letter_val(letter):
    if(letter == 'S'):
        return ord('a')
    elif(letter == 'E'):
        return ord('z')
    else:
        return ord(letter)

def has_path(_from, _to):
    r_f, c_f = _from
    r_t, c_t = _to
    letter_from = map[r_f][c_f]
    letter_to = map[r_t][c_t]
    val_from = get_letter_val(letter_from)
    val_to = get_letter_val(letter_to)
    if(val_to - val_from > -2):
        return True
    else:
        return False

with open('./day12/data.txt') as f:
    map = []
    queue = []
    visited = []
    for line in f:
        line = line.strip()
        map.append([x for x in line])

    distances = [[len(map)*len(map[0]) for y in x] for x in map]

    for row in range(len(map)):
        for col in range(len(map[0])):
            if(map[row][col]== 'E'):
                distances[row][col] = 0
            queue.append((row, col))

    done = False
    while(not done):
        queue.sort(key=lambda x: distances[x[0]][x[1]])
        start = queue.pop(0)
        x,y = start
        start_distance = distances[x][y]
        start_letter = map[x][y]
        start_height = get_letter_val(start_letter)

        if(start_letter == 'a'):
            done=True
            print(start_distance)
            break

        for next in [(x-1,y), (x,y-1), (x+1,y), (x,y+1)]:
            if(next not in visited and next in queue and has_path(start,next)):
                row, col = next
                next_distance = start_distance + 1
                curr_distance = distances[row][col]
                if(next_distance < curr_distance):
                    distances[row][col] = next_distance
        visited.append(start)