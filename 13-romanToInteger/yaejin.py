def romanToInt(s: str) -> int:
    
    result = 0
    newStr = s

    if s.find('IV') >= 0:
        result += 4
        newStr = newStr.replace('IV','')
    if s.find('IX') >= 0:
        result += 9
        newStr = newStr.replace('IX','')
    if s.find('XL') >= 0:
        result += 40
        newStr = newStr.replace('XL','')
    if s.find('XC') >= 0:
        result += 90
        newStr = newStr.replace('XC','')
    if s.find('CD') >= 0:
        result += 400
        newStr = newStr.replace('CD','')
    if s.find('CM') >= 0:
        result += 900
        newStr = newStr.replace('CM','')
    
    print(newStr)
    print(len(newStr))

    for i in range(0, len(newStr)):
        print(newStr[i])
        if newStr[i] == 'I':
            result += 1
        elif newStr[i] == 'V':
            result += 5
        elif newStr[i] == 'X':
            result += 10
        elif newStr[i] == 'L':
            result += 50
        elif newStr[i] == 'C':
            result += 100
        elif newStr[i] == 'D':
            result += 500
        elif newStr[i] == 'M':
            result += 1000
        else:
            result += 0
    
    print(result)
    return result

romanToInt('MCMXCIV')