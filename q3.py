def find_ID(email):
    """Check if duke address and if so, return user name from the input email address.  Otherwise return None   
    """
    ### BEGIN SOLUTION
    info=email.split('@')
    if(  (len(info)==2)  and  info[1]=='duke.edu'):
        return info[0]
    else:
        return None
    ### END SOLUTION
