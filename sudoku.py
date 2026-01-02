rows = 9
cols = 9


def row_clear(x,y):
    for k in range(9):
        if grid_to_solve[x][y] in potential_grid[x][k]:
            potential_grid[x][k].remove(grid_to_solve[x][y])
            #print(potential_grid[x][k])
            #print(f"Removed {grid_to_solve[x][y]}")
    
def col_clear(x,y):
    for l in range(9):
        if grid_to_solve[x][y] in potential_grid[l][y]:
            potential_grid[l][y].remove(grid_to_solve[x][y])
            #print(potential_grid[l][y])
            #print(f"Removed {grid_to_solve[x][y]}")

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
[5,3,0,0,0,4,2,0,0],
[0,0,0,9,0,0,7,0,4],
[0,0,0,0,1,2,6,0,5],
[0,0,4,0,6,3,1,0,0],
[9,0,3,0,4,7,0,6,0],
[6,0,0,0,0,0,0,0,2],
[0,0,0,0,0,0,0,0,0],
[0,2,6,4,0,9,8,0,0],
[0,9,1,5,0,0,0,0,0]
]

potential_grid = [[[1,2,3,4,5,6,7,8,9] for i in range(cols)] for j in range(rows)]



for i in range(9):
    for j in range(9):
        if(grid_to_solve[i][j] != 0):
            row_clear(i, j)
            col_clear(i, j)
            section_clear(i,j)
            potential_grid[i][j] = [grid_to_solve[i][j]]




print(potential_grid)