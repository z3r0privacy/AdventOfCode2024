
def is_decreasing(numbers, dampener=False):
    for i,n in enumerate(numbers[1:]):
        if n >= numbers[i] or abs(n-numbers[i]) > 3:
            if not dampener:
                return False
            else:
                p1 = numbers[:i] + numbers[i+1:]
                p2 = numbers[:i+1] + numbers[i+2:]
                return is_decreasing(p1) or is_decreasing(p2)
    return True

def is_increasing(numbers, dampener=False):
    for i,n in enumerate(numbers[1:]):
        if n <= numbers[i] or abs(n-numbers[i]) > 3:
            if not dampener:
                return False
            else:
                p1 = numbers[:i] + numbers[i+1:]
                p2 = numbers[:i+1] + numbers[i+2:]
                return is_increasing(p1) or is_increasing(p2)
    return True

def count_safe(number_sets, dampener=False):
    cnt = 0
    for numbers in number_sets:
        if is_decreasing(numbers, dampener=dampener) or is_increasing(numbers, dampener=dampener):
            cnt += 1
    return cnt

if __name__ == "__main__":
    number_sets = [[int(e) for e in l.split(" ")] for l in open("inputs\\day02.txt").readlines()]
    num_safe = count_safe(number_sets)
    print(f"Safe: {num_safe}")
    num_safe2 = count_safe(number_sets, dampener=True)
    print(f"Safe2: {num_safe2}")
