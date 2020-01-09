def cubics(n):
    """Compute the cubics of numbers from 1 to n, such that the 
    ith element of the returned list equals i^3.
    
    """
    ### BEGIN SOLUTION
    if((n<=0)|(type(n)!=int)):
        raise ValueError('n must be a positive integer') 
    
    return [i**3 for i in range (1,n+1)]
    ### END SOLUTION
   
def sum_of_cubics(n):
    """Compute the sum of the cubics of numbers from 1 to n."""
    ### BEGIN SOLUTION
    return sum(cubics(n))
    ### END SOLUTION
