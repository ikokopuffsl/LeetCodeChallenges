import math
def climbStairs(n):
    """
    This is basically Fibonacci! Don't know why it came out to be fibonacci tho.
    """
    
    n1 = 1
    n2 = 2

    if n == 1:
        return n1
    elif n == 2:
        return n2

    for i in range(2, n):
        nextVal = n1 + n2
        n1 = n2
        n2 = nextVal

    return nextVal

climbStairs(6)
    