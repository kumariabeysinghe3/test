def is_valid(grid, row, col):
    # Check if position is inside grid bounds
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def count_adjacent_mines(grid, row, col):
    count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),   
        (0, -1),          (0, 1),     
        (1, -1), (1, 0), (1, 1)       
    ]

    for d in directions:
        new_row = row + d[0]
        new_col = col + d[1]

        if is_valid(grid, new_row, new_col):
            if grid[new_row][new_col] == "#":
                count += 1
    return count

def minesweeper(grid):
    result = []

    for r in range(len(grid)):
        new_row = []
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                new_row.append("#")
            else:
                mines = count_adjacent_mines(grid, r, c)
                new_row.append(mines)
        result.append(new_row)
    return result

#test grid to see the output
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

print(minesweeper(grid))