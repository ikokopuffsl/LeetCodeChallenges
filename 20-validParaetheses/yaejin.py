def isValid(s):
    
    result = False

    if len(s) == 0 or s[0] == "":
        result = True
        return result
    
    if s.count("(") == s.count(")") and s.count("[") == s.count("]") and s.count("{") == s.count("}"):

        for i in range(0, len(s)):
            if s[i] == "(":
                for i2 in range(i + 1, len(s), 2):
                    if s[i2] == ")":
                        result = True
                        break
                    else:
                        result = False
                if result == False:
                    return result
            elif s[i] == "{":
                for i2 in range(i + 1, len(s), 2):
                    if s[i2] == "}":
                        result = True
                        break
                    else:
                        result = False
                if result == False:
                    return result
            elif s[i] == "[":
                for i2 in range(i + 1, len(s), 2):
                    if s[i2] == "]":
                        result = True
                        break
                    else:
                        result = False
                if result == False:
                    return result

    return result

isValid("{[]}")