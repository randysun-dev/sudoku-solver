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

# Define potential grid of "notes" with all possible numbers for each square.
# This gets narrowed down as sudoku strategies are applied.
potential_grid = [[[1,2,3,4,5,6,7,8,9] for i in range(cols)] for j in range(rows)]

# Fixed variable definitions
rows = 9
cols = 9

# Parses through row and removes numbers from potential_grid that already
# occur in the solved section. Also checks if each number has only one possible
# spot on the row and if so fills it in.
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

        
# Parses through column and removes numbers from potential_grid that already
# occur in the solved section. Also checks if each number has only one possible
# spot on the column and if so fills it in.
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

# Parses through subgrid and removes numbers from potential_grid that already
# occur in the solved section. Also checks if each number has only one possible
# spot on the subgrid and if so fills it in.
def section_clear(x,y):
    allNum = []
    subsectionX = x // 3
    subsectionY = y // 3
    #print(f"X: {x}, Y: {y}, subX:{subsectionX}, subY:{subsectionY}")
    for m in range(3):
        for n in range(3):
            allNum += (potential_grid[subsectionX*3+m][subsectionY*3+n])
            if grid_to_solve[x][y] in potential_grid[subsectionX*3+m][subsectionY*3+n]:
                potential_grid[subsectionX*3+m][subsectionY*3+n].remove(grid_to_solve[x][y])
    for l in range(9):
        #print(allNum.count(l+1))
        if allNum.count(l+1) == 1 and (l+1 in potential_grid[l][y]):
            for o in range(3):
                for p in range(3):
                    if l+1 in potential_grid[subsectionX*3+o][subsectionY*3+p]:
                        potential_grid[subsectionX*3+o][subsectionY*3+p] = [l+1]
                        grid_to_solve[subsectionX*3+o][subsectionY*3+p] = l+1






# Runs the program, iterates through each square and runs sudoku strategy.
# If the program determines that it is "stuck", where it is making no more
# progress on the puzzle, it ends the loop and returns the final result.
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

if prevSum == 81:
    print("Solved!")
else:
    print("Failed to Solve")
    