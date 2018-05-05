def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    xs = []
    for x in range(left, right + 1):
        y = x 
        while y != 0: 
            d = y%10 
            if(d==0):
                break
            if(x % d != 0):
                break
            y = y//10 
    	else:
            xs.append(x)
    print(xs)

selfDividingNumbers(1,10000)
