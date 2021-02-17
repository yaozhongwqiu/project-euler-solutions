# problem 1

def solution_1 () :
    multiples_of_3 = list(range(0, 1000, 3))
    multiples_of_5 = list(range(0, 1000, 5))
    x = list(set(multiples_of_3 + multiples_of_5))
    return(sum(x))