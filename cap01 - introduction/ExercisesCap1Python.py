def sumZeroToTen():
    sumUntilTen = 0
    for n in range(11):
        sumUntilTen = sumUntilTen + n
        print(sumUntilTen)
    return sumUntilTen


def multipleZeroToTen():
    multiple = 1
    for n in range(11):
        if n != 0:
            multiple = multiple * n
            print(multiple)
    return multiple


