def turn_right(curr_dir:tuple[int,int]) -> tuple[int,int]:
    if curr_dir == (0, -1): return (1,0)
    if curr_dir == (1, 0): return (0, 1)
    if curr_dir == (0, 1): return (-1, 0)
    if curr_dir == (-1, 0): return (0, -1)
    raise ValueError()

def get_new_pos(map:list[list[chr]], curr_pos:tuple[int,int], curr_dir:tuple[int, int]) -> tuple[tuple[int, int],tuple[int, int]]:
    new_pos = (curr_pos[0]+curr_dir[0], curr_pos[1]+curr_dir[1])
    if new_pos[1] < 0 or new_pos[1] >= len(map) or new_pos[0] < 0 or new_pos[0] >= len(map[new_pos[1]]):
        return None, None
    if map[new_pos[1]][new_pos[0]] == "#":
        new_dir = turn_right(curr_dir)
        return get_new_pos(map, curr_pos, new_dir)
    return new_pos, curr_dir

def check_circle(map:list[list[chr]], start_pos:tuple[int,int]) -> bool:
    curr_dir = (0, -1)
    curr_pos = start_pos
    visited = set()
    while True:
        new_pos, curr_dir = get_new_pos(map, curr_pos, curr_dir)
        if new_pos is None:
            return False
        curr_state = (new_pos[0], new_pos[1], curr_dir[0], curr_dir[1])
        if curr_state in visited:
            return True
        visited.add(curr_state)
        curr_pos = new_pos

if __name__ == "__main__":
    map = open("inputs\\day06.txt").readlines()
    curr_pos = (-1, -1)
    start_pos = None
    curr_dir = (0, -1)
    all_positions = set()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                curr_pos = (x,y)
                start_pos = (x,y)
    all_positions.add(curr_pos)
    while True:
        new_pos, curr_dir = get_new_pos(map, curr_pos, curr_dir)
        if new_pos is None:
            break
        all_positions.add(new_pos)
        curr_pos = new_pos

    count_2 = 0
    for y in range(len(map)):
        #print(f"Processing line {y}")
        for x in range(len(map[y])):
            if map[y][x] != ".":
                continue
            orig_str = map[y]
            l = list(orig_str)
            l[x] = '#'
            map[y] = "".join(l)
            if check_circle(map, start_pos):
                count_2 += 1
            map[y] = orig_str
    
    print(f"Num Pos (1): {len(all_positions)}")
    print(f"Num Loops (2): {count_2}")
