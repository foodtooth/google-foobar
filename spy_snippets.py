def answer(document, searchTerms):
    documentList = document.split(' ')
    maxLength = len(documentList)
    minLength = len(searchTerms)
    for i in range(minLength, maxLength + 1):
        for j in range(0, maxLength - i + 1):
            if len(set(documentList[j:j + i]) & set(searchTerms)) == minLength:
                return ' '.join(documentList[j:j + i])


if __name__ == "__main__":
    print answer("many google employees can program", ["google", "program"])
