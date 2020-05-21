def mySqrt(x):
    result = 0
        
    if x == 1:
        return 1
    
    for i in xrange(0, x):
        if i * i <= x:
            result = i
        else:
            return result
    
    return result

mySqrt(1)