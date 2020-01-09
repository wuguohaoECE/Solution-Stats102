def myfactorial(num):
    '''Calculate the Factorial of the input num
    the output is an int
    
    For instance, "four factorial" is written as "4!" and means 1×2×3×4 = 24. 
    In general, n! ("enn factorial") means the product of all the whole numbers from 1 to n; 
    that is, n! = 1×2×3×...×n.
    '''
    if(type(num)!=int):
        raise VauleError('input is not an integer')
    if(num<=0):
        raise VauleError('input is not an integer')
    '''start your code here, num is a positive integer here'''
    ### BEGIN SOLUTION    
    myfactorial=1
    for i in range(1,num+1):
        myfactorial=myfactorial*i
    return myfactorial

    ### END SOLUTION
    '''end your code'''
