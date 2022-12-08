
def get_viewing_distance(val, heights):
    max = val

grid = []
num_visible = 0
with open('./day08/testdata.txt') as f:
    for line in f:
        grid.append([x for x in line.strip()])
    dim = len(grid)
    for i in range(dim): #row
        for j in range(dim): #col
            if (i == 0 or j == 0 or i == dim-1 or j == dim-1):
                continue
            val = grid[i][j]
            col = [grid[x][j] for x in range(dim)]
            row = grid[i]
            # left = row[:j]
            left = row[-dim+j-1:-dim-1:-1]
            right = row[j+1:]
            # top = col[:i]
            top = col[-dim+i-1:-dim-1:-1]
            bottom = col[i+1:]
            # compute viewing distances here
            
            # [get_viewing_distance(val, x) for x in [left, right, top, bottom]]
            # if (max(left) < val or max(right) < val or max(top) < val or max(bottom) < val):
            #     num_visible += 1
print(num_visible)