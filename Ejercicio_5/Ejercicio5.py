def fiboTree(n):
    result = [0, 1]
    for i in range(2, n):
        result[i % 2] = (result[(i - 1) % 2] + 1) ^ (result[(i - 2) % 2] + 1)#principio de colon
    if result[(n - 1) % 2] > 0:
        return True
    else:
        return False


print(fiboTree(200))
