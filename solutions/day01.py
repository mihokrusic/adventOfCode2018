import re

def solve(input, part):
    changes = list(map(int, re.findall(r'([+|-]\d+)', input)))
    if part == 1:
        return sum(list(changes))
    dt = dict()
    dt[0] = 1
    current = 0
    ix = 0
    while True:
        current += changes[ix]
        if current in dt:
            return current
        else:
            dt[current] = 1
        ix += 1
        if ix == len(changes):
            ix = 0

    return -1


