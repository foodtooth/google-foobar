def answer(population, x, y, strength):
    y_length = len(population)
    x_length = len(population[0])

    if x in range(0, x_length) and y in range(0, y_length) and population[y][x] != -1:
        if population[y][x] <= strength:
            population[y][x] = -1
            answer(population, x + 1, y, strength)
            answer(population, x - 1, y, strength)
            answer(population, x, y + 1, strength)
            answer(population, x, y - 1, strength)
    return population

if __name__ == "__main__":
    print answer([[1, 2, 3], [2, 3, 4], [3, 2, 1]], 0, 0, 2)
    print answer([[1]], 0, 0, 2)
