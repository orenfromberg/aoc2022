grid = []
num_visible = 0
with open('./day08/data.txt') as f:
    for line in f:
        grid.append([x for x in line.strip()])
    dim = len(grid)
    for i in range(dim): #row
        for j in range(dim): #col
            if (i == 0 or j == 0 or i == dim-1 or j == dim-1):
                num_visible += 1
            else:
                val = grid[i][j]
                col = [grid[x][j] for x in range(dim)]
                row = grid[i]
                left = row[:j]
                right = row[j+1:]
                top = col[:i]
                bottom = col[i+1:]
                if (max(left) < val or max(right) < val or max(top) < val or max(bottom) < val):
                    num_visible += 1
print(num_visible)