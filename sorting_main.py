import time

from auxiliary_functions import list_generator, result_visualiser
from sorting_methods import heap_sort, quick_sorting, default_sorting

"""
1- сгенерировать массив
2- показать массив
3- функция быстрой сортировки
4- функция пирамидальной сортировки
5- настроить замеры времени для каждой функции сортировки
"""


# def lambda_function(a, b): return a - b
# def lambda_function(a, b): return 1 if a[0] < b[0] else -1 if a[0] > b[0] else 0
# def lambda_function(a, b): return 1 if a[1] < b[1] else -1 if a[1] > b[1] else 0
# def lambda_function(a, b): return 1 if a[2] < b[2] else -1 if a[2] > b[2] else 0

generated_list = [
    list_generator(-5, 10),
    # [('dave', 'B', 5), ('cane', 'B', 12), ('john', 'A', 15), ('grut', 'C', 25), ('amon', 'S', 19), ('donald', 'X', 20)],
    # [('IT_VLAN', 320), ('Mngmt_VLAN', 99), ('User_VLAN', 1010), ('DB_VLAN', 11), ('DOM_VLAN', 120), ('St_VLAN', 66),
    #  ('York_VLAN', 8080), ('CV_VLAN', 111)]
]

lambda_functions = [
    # lambda a, b: a - b,
    lambda a, b: 1 if a < b else -1 if a > b else 0,
    # lambda a, b: 1 if a[1] < b[1] else -1 if a[1] > b[1] else 0

]


sorting_functions_variants = [
    # (default_sorting, generated_list, lambda_functions),
    # (quick_sorting, generated_list, lambda_functions),
    (heap_sort, generated_list, lambda_functions)
]

if __name__ == '__main__':

    for fnc, data, lmd in sorting_functions_variants:
        result_visualiser(fnc, data, lmd)
        time.sleep(0.8)
