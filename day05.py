from typing import Any


def check_order(update:list[int], rules:dict[int,list[int]]) -> bool:
    rev_update = update[::-1]
    for i,n in enumerate(rev_update):
        if n in rules:
            prev = rev_update[i+1:]
            for not_prev in rules[n]:
                if not_prev in prev:
                    return False
    return True

def _get_index(l:list[Any], item:Any) -> int:
    try:
        return l.index(item)
    except ValueError:
        return -1

def fix_order(update:list[int], rules:dict[int,list[int]]) -> list[int]:
    new_update = []
    for n in update:
        if n in rules:
            if any(not_prev in new_update for not_prev in rules[n]):
                pos = min(new_update.index(not_prev) for not_prev in rules[n] if not_prev in new_update)
                new_update.insert(pos, n)
            else:
                new_update.append(n)
        else:
            new_update.append(n)
    return new_update

if __name__ == "__main__":
    rule_parsing = True
    rules = {}
    updates = []
    for line in open("inputs\\day05.txt").readlines():
        line = line.strip()
        if line == "":
            if not rule_parsing: break
            rule_parsing = False
            continue
        if rule_parsing:
            nums = [int(n) for n in line.split("|")]
            if nums[0] not in rules:
                rules[nums[0]] = []
            rules[nums[0]].append(nums[1])
        else:
            updates.append([int(n) for n in line.split(",")])

    sum_1 = 0
    sum_2 = 0
    for update in updates:
        if check_order(update, rules):
            sum_1 += update[int(len(update)/2)]
        else:
            fixed = fix_order(update, rules)
            sum_2 += fixed[int(len(fixed)/2)]

    print(f"Sum (1): {sum_1}")
    print(f"Sum (2): {sum_2}")
