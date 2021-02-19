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
    
def solution_2 () :
    s = 0
    x_0 = 1
    x_1 = 1
    while True : 
        x_2 = x_0 + x_1 
        if x_2 > 4000000 :
            break
        if x_2 % 2 == 0 :
            s = s + x_2
        x_0 = x_1 
        x_1 = x_2
    return(s)

def solution_3():
    # Ryan's solution
    a, b = 1, 1 
    f = [a, b]
    
    while f[-1] < 4000000:
        f.append(a + b)
        b = f[-1]
        a = f[-2]
    
    f.pop() # Need to remove last item in list 
    f_even = [i for i in f if i%2==0]
    return sum(f_even)
    
%timeit solution_1()
%timeit solution_2()



#30.7 µs ± 318 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#3.89 µs ± 46.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)