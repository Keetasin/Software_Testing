def gridChallenge(grid):
    
    grid = [sorted(row) for row in grid]
    print(grid)
    t = tuple(zip(*grid))
    print(t)
    if all([row[i] <= row[i + 1] for row in t for i in range(len(row) - 1)]):
        return 'YES'
    return 'NO'


