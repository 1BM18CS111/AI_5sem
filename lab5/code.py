def clean(floor):
    for x in range(len(floor)):
        print('Floor {} : '.format(x+1))
        for y in range(len(floor[0])):
            floor = print_floor(floor, x, y)
        print()
def print_floor(floor, row, col): 
    if floor[row][col]:
        floor[row][col] = 0
        print(' Cleaned ', end = ' ')
    else: print(' Already Cleaned ', end = ' ')
    return floor
