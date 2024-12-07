def try_get_value(matrix:list[list[chr]], x:int, y:int) -> chr:
    if y < 0 or y >= len(matrix):
        return None
    if x < 0 or x >= len(matrix[y]):
        return None
    return matrix[y][x]

def test_word(matrix:list[list[chr]], x:int, y:int, word:str, dir:tuple[int,int]) -> bool:
    for c in word:
        if try_get_value(matrix, x, y) != c:
            return False
        x += dir[0]
        y += dir[1]
    return True

def find_word(matrix:list[list[chr]], x:int, y:int, word:str) -> int:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1,0),
        (1,1)
    ]
    found = 0
    for d in directions:
        if test_word(matrix, x, y, word, d):
            found += 1
    return found

if __name__ == "__main__":
    word_1 = "XMAS"
    word_2 = "MAS"
    matrix = open("inputs\\day04.txt").readlines()
    found_1 = 0
    found_2 = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            found_1 += find_word(matrix, x, y, word_1)
            if matrix[y][x] == "A":
                mas_cnt = 0
                if test_word(matrix, x-1, y-1, word_2, (1,1)):
                    mas_cnt += 1
                if test_word(matrix, x+1, y-1, word_2, (-1, 1)):
                    mas_cnt += 1
                if test_word(matrix, x-1, y+1, word_2, (1, -1)):
                    mas_cnt += 1
                if test_word(matrix, x+1, y+1, word_2, (-1, -1)):
                    mas_cnt += 1
                if mas_cnt == 2:
                    found_2 += 1


    print(f"Found (1): {found_1}")
    print(f"Found (2): {found_2}")
