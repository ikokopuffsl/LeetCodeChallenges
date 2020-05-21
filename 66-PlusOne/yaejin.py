def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digitsToStr = ''
    result = []

    for i in range(len(digits)):
        digitsToStr += str(digits[i])

    strToNum = int(digitsToStr) + 1

    numToStr = str(strToNum)

    for i in range(len(numToStr)):
        result.append(int(numToStr[i]))

    print(result)
    return result


plusOne([1,2,3])

    