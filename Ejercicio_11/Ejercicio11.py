def StrobogrammaticNum(n):
    result = []
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middle_num = StrobogrammaticNum(n-2)
    for x in middle_num:
        result.append("1"+ x +"1")
        result.append("8" + x + "8")
        result.append("9" + x + "6")
        result.append("6" + x + "9")
    return result





