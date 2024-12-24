
def is_in_range(city:list[str], p:tuple[int,int]) -> bool:
    if p[1] < 0 or p[1] >= len(city):
        return False
    if p[0] < 0 or p[0] >= len(city[p[1]]):
        return False
    return True


# 387 too high

if __name__ == "__main__":
    city = [s.strip() for s in open("inputs\\day08.txt", "r").readlines()]
    antennas = {}
    for y in range(len(city)):
        for x in range(len(city[y])):
            a = city[y][x]
            if a != ".":
                if a not in antennas:
                    antennas[a] = []
                antennas[a].append((x,y))
    
    antinodes_1 = set()
    antinodes_2 = set()

    for locs in antennas.values():
        for l in locs:
            antinodes_2.add(l)

    for a,locs in antennas.items():
        for i in range(len(locs)):
            for j in range(len(locs[i+1:])):
                dx = locs[i][0] - locs[i+1+j][0]
                dy = locs[i][1] - locs[i+1+j][1]
                p1 = (locs[i][0]+dx, locs[i][1]+dy)
                p2 = (locs[i+1+j][0]-dx, locs[i+1+j][1]-dy)
                if is_in_range(city, p1):
                    antinodes_1.add(p1)
                if is_in_range(city, p2):
                    antinodes_1.add(p2)
                while is_in_range(city, p1):
                    antinodes_2.add(p1)
                    p1 = (p1[0]+dx, p1[1]+dy)
                while is_in_range(city, p2):
                    antinodes_2.add(p2)
                    p2 = (p2[0]-dx, p2[1]-dy)

    print(f"Num Antinodes: {len(antinodes_1)}")
    print(f"Num Antinodes: {len(antinodes_2)}")
    """
    not_printed = []
    for y in range(len(city)):
        print(f"{y:02d}: ", end="")
        for x in range(len(city[y])):
            is_a = city[y][x] != "."
            is_n = (x,y) in antinodes
            if is_a:
                print(city[y][x], end=" ")
                if is_n:
                    not_printed.append((x,y))
            elif is_n:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

    print("overlapping:")
    print("\n".join(str(np) for np in not_printed))
    """