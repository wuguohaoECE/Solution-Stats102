def Collatz(n):
    """For input n (must be a positive integer), compute a list of numbers in reverse order, that form a Collatz conjecture sequence.
  
    """
    ### BEGIN SOLUTION
    if(type(n)!=int):
        raise ValueError("n must be a positive integer")
    if(n<=0):
        raise ValueError("n must be a positive integer")
    output=[n]
    currentnum=n
    while (currentnum!=1):
        if(currentnum%2==0):
            currentnum=int(currentnum/2)
        else:
            currentnum=(3*currentnum+1)
        output.append(currentnum)
    return output    
    ### END SOLUTION
