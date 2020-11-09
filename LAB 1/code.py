def notClean(floor):
    for row in floor:
        if 1 in row:
            return True;
    return False
    
 def clean(floor, i, j):
    goRight = True
    
    while notClean(floor):
        # Print Floor
        print_floor(floor, i, j)
        # Clean
        if floor[i][j]:
            floor[i][j] = 0;
        # Decide Direction and Move (Zig-Zag)
        if j == len(floor[i])-1 and goRight:
            i, right = (i + 1) % len(floor), False
            continue
        elif j == 0 and not goRight:
            i, right = (i + 1) % len(floor), True
            continue
        else:
            j = j + 1 if goRight else j - 1
        
    # Cleaned Floor
    print_floor(floor, -1, -1)

def print_floor(floor, curr_row, curr_col): 
    for row in range(len(floor)):
        for col in range(len(floor[row])):
            if (curr_row, curr_col) == (row, col):
                print(" >", floor[row][col], "< ", end='', sep='')
            else:
                print("  ", floor[row][col], "  ", end='', sep='')
        print()
    print()

N = int(input('Enter number of rows: '))
M = int(input('Enter number of cols: '))

floor = []
print('Enter the rows')
for i in range(N):
    row = list(map(int, input().split()))
    floor.append(row)
    
start_row = int(input('Enter starting row (0-indexed): '))
start_col = int(input('Enter starting column (0-indexed): '))
clean(floor, start_row, start_col)


    
