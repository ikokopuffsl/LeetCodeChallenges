def reverse(x: int) -> int:
    
    result = 0
    converted = str(x)

    if x == 0  or x < 10 and x > -10:
        return x
    elif x >= 10:
        result = int(converted[::-1])
    else:
        noMinus = converted[1:]
        posResult = noMinus[::-1]
        strResult = "-" + posResult
        result = int(strResult)

    if result > 2**31 or result < -2**31:
        return 0

    return result

reverse(-123)
