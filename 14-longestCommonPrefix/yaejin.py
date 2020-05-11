def longestCommonPrefix(strs):

    srtedList = sorted(strs)
    commonFlag = True
    result = ""
    minLen = min(len(word)for word in strs)
    print(minLen)

    while commonFlag == True:
        for i in range(0, minLen):
            if srtedList[0][i] == srtedList[len(srtedList)-1][i]:
                result += srtedList[0][i]
            else:
                commonFlag = False
                print(result)
                return result

examplelist = [""]

longestCommonPrefix(examplelist)
        