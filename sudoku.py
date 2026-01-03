rows = 9
cols = 9

#
def row_clear(x,y):
    allNum = []
    for k in range(9):
        allNum += (potential_grid[x][k])
        if grid_to_solve[x][y] in potential_grid[x][k]:
            potential_grid[x][k].remove(grid_to_solve[x][y])
            #print(potential_grid[x][k])
            #print(f"Removed {grid_to_solve[x][y]}")
    #print(allNum)
    for l in range(9):
        #print(allNum.count(l+1))
        if allNum.count(l+1) == 1:
            for m in range(9):
                if l+1 in potential_grid[x][m]:
                    potential_grid[x][m] = [l+1]
                    grid_to_solve[x][m] = l+1

        

def col_clear(x,y):
    allNum = []
    for k in range(9):
        allNum += (potential_grid[k][y])
        if grid_to_solve[x][y] in potential_grid[k][y]:
            potential_grid[k][y].remove(grid_to_solve[x][y])
            #print(potential_grid[l][y])
            #print(f"Removed {grid_to_solve[x][y]}")
    for l in range(9):
        #print(allNum.count(l+1))
        if allNum.count(l+1) == 1 and (l+1 in potential_grid[l][y]):
            for m in range(9):
                if l+1 in potential_grid[m][y]:
                    potential_grid[m][y] = [l+1]
                    grid_to_solve[m][y] = l+1


def section_clear(x,y):
    subsectionX = x // 3
    subsectionY = y // 3
    #print(f"X: {x}, Y: {y}, subX:{subsectionX}, subY:{subsectionY}")
    for m in range(3):
        for n in range(3):
            if grid_to_solve[x][y] in potential_grid[subsectionX*3+m][subsectionY*3+n]:
                potential_grid[subsectionX*3+m][subsectionY*3+n].remove(grid_to_solve[x][y])


# Input sudoku grid
# 9x9
grid_to_solve = [
[0,0,1,6,0,0,0,8,9],
[0,0,0,0,0,0,3,1,0],
[0,4,0,0,0,0,7,5,0],
[0,0,0,0,5,7,2,3,0],
[0,1,8,0,0,0,0,0,0],
[0,0,0,2,0,0,6,9,1],
[0,0,0,7,6,3,0,0,0],
[9,6,0,4,0,0,8,0,3],
[3,0,0,0,0,8,0,0,5]
]

potential_grid = [[[1,2,3,4,5,6,7,8,9] for i in range(cols)] for j in range(rows)]


prevSum = 0
while True:
    for i in range(9):
        for j in range(9):
            if(grid_to_solve[i][j] != 0):
                row_clear(i, j)
                col_clear(i, j)
                section_clear(i,j)
                potential_grid[i][j] = [grid_to_solve[i][j]]

    sum = 0
    for x in range(9):
        for y in range(9):
            currentLength = len(potential_grid[x][y])
            if currentLength == 1:
                grid_to_solve[x][y] = potential_grid[x][y][0]
            sum += currentLength
    if sum == prevSum:
        break
    else:
        prevSum = sum


for i in range(9):
    for j in range(9):
        print(potential_grid[i][j], end=' ')
    print('')

print(grid_to_solve)
    