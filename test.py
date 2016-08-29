import operator


def answer(names):
    d = {s: getValue(s) for s in names}
    d2 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    repareList = []
    for tupleItem in d2:
        if len(repareList) == 0:
            repareList.append(tupleItem)
        elif len(repareList) == 1:
            if tupleItem[1] == repareList[0][1]:
                repareList.append(tupleItem)
            else:
                repareList[0] = tupleItem
        else:
            if tupleItem[1] == repareList[0][1]:
                repareList.append(tupleItem)
            else:
                orderedList = reorder(repareList)
                d2[d2.index(tupleItem) - len(orderedList):d2.index(tupleItem)] = orderedList
                repareList = [tupleItem]
    if len(repareList) >= 2:
        orderedList = reorder(repareList)
        d2[-(len(repareList)):] = orderedList
    print [item[0] for item in d2]


def reorder(l):
    return sorted(l, key=lambda i: i[0], reverse=True)


def getValue(s):
    sum = 0
    for c in s:
        sum += ord(c) % 32
    return sum

if __name__ == "__main__":
    answer(['ab', 'cc', 'ae'])
