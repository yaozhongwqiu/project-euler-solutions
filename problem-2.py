#problem 2

import numpy as np

def solution_1 () :
    # even fibonacci numbers occur at every 3rd natural number
    # e.g. 1, 1, *2*, 3, 5, *8*, et cetera
    # the following method is based on Binet's formula
    varphi = (1 + np.sqrt(5))/2
    psi = 1 - varphi 
    def helper (n) : 
        # calculate the 3*n-th fibonacci number
        return((varphi ** (3*n) - psi ** (3*n))/np.sqrt(5))
    x, n = [], 1
    while True :
        a = helper(n) 
        if (a < 4e6) :
            x.append(a)
            n = n + 1
        else :
            break
    return(int(sum(x))) # approximation
    
%timeit solution_1()

#29.8 µs ± 133 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)