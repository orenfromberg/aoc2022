
def get_viewing_distance(val, heights):
    num_trees = 0
    for i in heights:
        if(val <= i):
            num_trees += 1
            break
        if(val > i):
            num_trees += 1
    return num_trees

scores = []
grid = []
with open('./day08/data.txt') as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])
    dim = len(grid)
    for i in range(dim): #row
        for j in range(dim): #col
            if (i == 0 or j == 0 or i == dim-1 or j == dim-1):
                continue
            val = grid[i][j]
            col = [grid[x][j] for x in range(dim)]
            row = grid[i]
            left = row[:j]
            left.reverse()
            right = row[j+1:]
            top = col[:i]
            top.reverse()
            bottom = col[i+1:]
            # compute viewing distances here
            l_d = get_viewing_distance(val, left)
            r_d = get_viewing_distance(val, right)
            t_d = get_viewing_distance(val, top)
            b_d = get_viewing_distance(val, bottom)
            score = l_d * r_d * t_d * b_d
            scores.append(score)

print(max(scores))