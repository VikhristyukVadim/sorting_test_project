import time

from secondary_functions import list_generator, result_visualiser
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
def lambda_function(a, b): return 1 if a[1] < b[1] else -1 if a[1] > b[1] else 0
# def lambda_function(a, b): return 1 if a[2] < b[2] else -1 if a[2] > b[2] else 0


# generated_list = list_generator(-5, 10)
# generated_list = [('dave', 'B', 5), ('cane', 'B', 12), ('john', 'A', 15)]
generated_list = [('IT_VLAN', 320), ('Mngmt_VLAN', 99), ('User_VLAN', 1010), ('DB_VLAN', 11)]

sorting_functions_variants = [
    default_sorting,
    quick_sorting,
    heap_sort
]

if __name__ == '__main__':

    for i in sorting_functions_variants:
        result_visualiser(i, generated_list, None)
        time.sleep(0.8)
