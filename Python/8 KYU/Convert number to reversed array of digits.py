def digitize(n):
    
    n_str = str(n)[::-1] 
    
    digit_str = [int(d) for d in n_str] 
    return digit_str