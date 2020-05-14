def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = 1
    index = 1

    if len(nums) == 0:
        return 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            length += 1
            nums[index] = nums[i]             
            index += 1

    print(length)
    return length


    

removeDuplicates([0,0,1,1,1,2,2,3,3,4])