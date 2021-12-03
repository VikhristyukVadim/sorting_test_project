from random import choice


def heapify(lst, heap_size, root_index, lambda_function):
    """ The index of the largest element is considered the root index """
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    """ If the left child of the root is a valid index and the element is greater than the current largest,
        update the largest element """

    if lambda_function is not None:
        """ Checking if the left child exists greater than the root """
        # if left_child < heap_size : print(">>>>>>>>>>>>>>>>",lambda_function(lst[left_child], lst[largest]))
        if left_child < heap_size and lambda_function(lst[left_child], lst[largest]) > 0:
            largest = left_child

        """ Ditto for the right child of the root """
        if right_child < heap_size and lambda_function(lst[right_child], lst[largest]) > 0:
            largest = right_child
    else:
        """ Checking if the left child exists greater than the root """
        if left_child < heap_size and lst[left_child] > lst[largest]:
            largest = left_child

        """ Ditto for the right child of the root """
        if right_child < heap_size and lst[right_child] > lst[largest]:
            largest = right_child

    """ If the largest element is no longer the root, they are swapped """
    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        """ Heapify the new root element to ensure it's the largest """
        heapify(lst, heap_size, largest, lambda_function)


def heap_sort(lst, lambda_function=None):
    """
    variant heapsort function
    :param lst: list
    :param lambda_function: optional user function
    :return: sorted list
    """
    n = len(lst)

    """ Create Max Heap from the list """
    """ The second argument means to stop the algorithm before element -1, i.e. before the first element of the list """
    """ 3rd argument means to iterate through the list in the opposite direction decreasing the counter i by 1 """
    for i in range(n, -1, -1):
        heapify(lst, n, i, lambda_function)

    """ Move the root Max Heap to the end of the list """
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0, lambda_function)
    return lst


def default_sorting(lst, lambda_function):
    """
    variant default sorting function
    :param lst: list
    :param lambda_function: optional user function
    :return: sorted list
    """
    res = sorted(lst)
    return res


def quick_sorting(lst, lambda_function=None):
    """
    variant quick sorting function
    :param lambda_function: optional user function
    :param lst: list of items
    :return: sorted list
    """

    if len(lst) <= 1:
        return lst
    else:
        q = choice(lst)

    e_lst = [q] * lst.count(q)
    if lambda_function is not None:
        l_lst = [n for n in lst if lambda_function(n, q) < 0]
        b_lst = [n for n in lst if lambda_function(n, q) > 0]
        res = quick_sorting(l_lst, lambda_function) + e_lst + quick_sorting(b_lst, lambda_function)
        return res
    else:
        l_lst = [n for n in lst if n < q]
        b_lst = [n for n in lst if n > q]
        res = quick_sorting(l_lst) + e_lst + quick_sorting(b_lst)
        return res
