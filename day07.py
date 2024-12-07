from math import log10, floor

def try_solve(target, curr_val, r_nums):
    if curr_val > target: return False
    if len(r_nums) == 0:
        return curr_val == target
    next_val = r_nums[0]
    new_remain = r_nums[1:]
    return try_solve(target, curr_val+next_val, new_remain) or try_solve(target, curr_val*next_val, new_remain)

def _combine(num1, num2):
    mult = 10**(floor(log10(num2))+1)
    return num1*mult + num2

def try_solve2(target, curr_val, r_nums):
    if curr_val > target: return False
    if len(r_nums) == 0:
        return curr_val == target
    next_val = r_nums[0]
    new_remain = r_nums[1:]
    return try_solve2(target, curr_val+next_val, new_remain) or try_solve2(target, curr_val*next_val, new_remain) or try_solve2(target, _combine(curr_val, next_val), new_remain)

if __name__ == "__main__":
    tests = []
    for line in open("inputs\\day07.txt").readlines():
        if not line.strip(): continue
        val, nums = line.split(": ")
        tests.append((int(val), [int(n) for n in nums.split(" ")]))
    res = 0
    res2 = 0
    for val, nums in tests:
        if try_solve(val, nums[0], nums[1:]):
            res += val
        elif try_solve2(val, nums[0], nums[1:]):
            res2 += val
    print(f"Sum (1): {res}")
    print(f"Sum (2): {res+res2}")
