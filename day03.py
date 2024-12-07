import re

if __name__ == "__main__":
    mem = open("inputs\\day03.txt").read()
    r_mul_ops = re.compile(r"mul\((?P<X>\d{1,3}),(?P<Y>\d{1,3})$")
    r_do = re.compile(r"do\($")
    r_dont = re.compile(r"don't\($")
    res1 = 0
    res2 = 0
    enabled = True
    for part in mem.split(")"):
        s = r_mul_ops.search(part)
        if s:
            s_val = int(s.group("X"))*int(s.group("Y"))
            res1 += s_val
            if enabled:
                res2 += s_val
        elif r_do.search(part):
            enabled = True
        elif r_dont.search(part):
            enabled = False
    print(res1)
    print(res2)