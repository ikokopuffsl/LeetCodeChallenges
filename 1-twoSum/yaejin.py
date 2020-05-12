def twoSum(nums, target):
    
    listLength = len(nums)
    
    indices = []
    
    for a in range(0, listLength - 1):
        
        for b in range(a + 1, listLength):
                
            if nums[a] + nums[b] == target:
                indices.append(a)
                indices.append(b)
    
    return indices

twoSum([2,7,11,15], 9)