def answer(words):
    wordsLength = len(words)
    order = ''
    if wordsLength == 1:
        order += words[0][0]
        return order
    else:
        for i in range(0, wordsLength + 1 - 2):
            j = min(len(words[i]), len(words[i + 1]))
            for k in range(0, j):
