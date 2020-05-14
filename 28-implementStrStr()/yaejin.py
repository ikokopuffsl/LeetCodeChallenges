def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # result = -1

    #     if len(needle) == 0:
    #         return 0

    #     result = haystack.find(needle)
        
    #     return result

    if len(needle) == 0:
        return 0
    
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

strStr('aaa', 'a')