# problem 1


def solution_1():
    multiples_of_3 = list(range(0, 1000, 3))
    multiples_of_5 = list(range(0, 1000, 5))
    x = list(set(multiples_of_3 + multiples_of_5))
    return(sum(x))


def solution_2():
    multiples_of_3 = [x for x in range(1000) if x % 3 == 0]
    multiples_of_5 = [x for x in range(1000) if x % 5 == 0]
    x = list(set(multiples_of_3 + multiples_of_5))
    return(sum(x))


def solution_3():
    # Ryan's solution
    max_num = 1000
    rng = range(max_num)
    return sum([i for i in rng if (i % 3 == 0 or i % 5 == 0)])


# benchmarks
%timeit solution_1()
%timeit solution_2()
%timeit solution_3()

# 23.8 µs ± 330 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 124 µs ± 3.82 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 94.7 µs ± 24.6 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
