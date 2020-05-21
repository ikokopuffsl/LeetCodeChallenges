def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #GOT A HELP FROM GOOGLE! ;)
    """
    contiguous subarray이기 때문애, 사실 nums를 한번만 쭉 훓으면서,
    그 바로 전까지의 모든 합이 현재 index의 value보다 큰지 작은지만 비교하면 된다.
    만약 현재 index가 더 크면 그게 새로운 subarray의 시작점이 되어 
    거기서부터 또 sum을 시작해서 끝까지 계속해간다.
    """

    maxSoFar = nums[0]
    maxEndingHere = 0

    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        if nums[i] > maxEndingHere + nums[i]:
            maxEndingHere = nums[i]
        else:
            maxEndingHere = maxEndingHere + nums[i]
        
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
        
    return maxSoFar
    

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    