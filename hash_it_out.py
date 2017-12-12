def main():
    answer([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165])


def answer(digest):
    message = []
    pn = 0
    for index, value in enumerate(digest):
        if index > 0:
            pn = message[index-1]
        message.append(exhaust(digest[index], pn))
    print(message)


def exhaust(num, prev_num=0):
    count = 0
    while True:
        t = (num + count * 256) ^ prev_num
        if t % 129 == 0:
            return t / 129
        else:
            count += 1


if __name__ == '__main__':
    main()
