def maxNumber(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


print(maxNumber(3, 4, 10))
