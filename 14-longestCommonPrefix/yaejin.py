def longestCommonPrefix(strs):
    
    if strs == []:
        return ""
    
    srtedList = sorted(strs)
    result = ""
    minLen = min(len(word)for word in strs)
    
    if minLen <= 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    for i in range(0, minLen):
        if srtedList[0][i] == srtedList[len(srtedList)-1][i]:
            result += srtedList[0][i]
        else:
            return result

    return result

examplelist = []

longestCommonPrefix(examplelist)
        