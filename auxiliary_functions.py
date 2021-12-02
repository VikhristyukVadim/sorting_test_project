import timeit
from random import randint


def list_generator(a, b):
    lst = {j * randint(1, 5) for j in range(a, b)}
    print("compiled list: ", [*lst])
    return [*lst]


def time_measure(fn, lst, lambda_function):
    start = timeit.default_timer()
    result_of_sorting = fn(lst, lambda_function)
    stop = timeit.default_timer()
    print(" " * 100)
    print("result_of_sorting", result_of_sorting)
    return stop - start


def result_visualiser(variant_of_sorting, data, lambda_function):
    for (dat, fnc) in list(zip(data, lambda_function)):
        spent_time = time_measure(variant_of_sorting, dat, fnc)
        print(variant_of_sorting.__name__, "<--- function wasted time : ", spent_time)
        print("-" * 100)
    print("." * 100)
