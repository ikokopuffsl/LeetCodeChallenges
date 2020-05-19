def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    
    if n == 1:
        return '1'
    else:
        prevStr = countAndSay(n - 1)
        counter = 1
        result = ''

        if len(prevStr) == 1:
            return '11'

        for i in range(1, len(prevStr)):
            if prevStr[i] == prevStr[i - 1]:
                counter += 1
            else:
                result += str(counter) + prevStr[i - 1]
                counter = 1
        
        result += str(counter) + prevStr[i]
        print(result)

        return result
        
countAndSay(30)