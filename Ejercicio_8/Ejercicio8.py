def minInterval(intervals, queries=[]):
    result = []
    for i in intervals:
        for x in queries:
            if i[1] >= x >= i[0]:
                res = abs(i[1] - i[0] + 1)
                result.append(res)
            if not i[1] >= x >= i[0]:
                result.append(-1)
        return result


print(minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
print(minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
