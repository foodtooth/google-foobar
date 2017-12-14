def main():
    print answer('aabb', 'ab')
    print answer('goodgooogoogfogoood', 'goo')
    print answer('dfdfdf', 'df')


def find_occur(str, sub):
    start = 0
    while True:
        loc = str.find(sub, start)
        if loc == -1:
            break
        else:
            yield loc
            start += loc + 1


def find(cur_ch, word):
    stack = [cur_ch]
    candidates = []
    while len(stack):
        cur_ch = stack.pop()
        for loc in find_occur(cur_ch, word):
            new_ch = cur_ch[:loc] + cur_ch[loc+len(word):]
            if new_ch not in stack:
                stack.append(new_ch)
        candidates.append(cur_ch)
    return candidates


def answer(chunk, word):
    can_set = set(find(chunk, word))
    candidates = [min(can_set, key=len)]
    for v in can_set:
        if v not in candidates and len(v) == len(candidates[0]):
            candidates.append(v)

    sorted(candidates)
    return candidates[0] if candidates else ''


if __name__ == '__main__':
    main()
