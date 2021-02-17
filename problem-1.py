#problem 1

def solution_1 () :
    multiples_of_3 = list(range(0, 1000, 3))
    multiples_of_5 = list(range(0, 1000, 5))
    x = list(set(multiples_of_3 + multiples_of_5))
    return(sum(x))

def solution_2 () : 
    multiples_of_3 = [x for x in range(1000) if x % 3 == 0]
    multiples_of_5 = [x for x in range(1000) if x % 5 == 0]
    x = list(set(multiples_of_3 + multiples_of_5))
    return(sum(x)) 

#benchmarks    
%timeit solution_1()
%timeit solution_2()

#27.6 µs ± 426 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#146 µs ± 1.01 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)