import random
from typing import Any


# def LPSort(arr: list, subsort) -> list:
#     ordering = [[] for _ in range(len(arr))]
#     min_val = None
#     max_val = None
#     ##GET MIN | MAX
#     for val in arr:
#         if min_val is None or min_val > val:
#             min_val = val
#         if max_val is None or max_val < val:
#             max_val = val
#
#     ##CALC PREDICTION FUNCTION
#     m = (min_val-max_val)/(-(len(arr)-1))
#     c = min_val
#
#     for val in arr:
#         index = int((val-c)/m)
#         ordering[index].append(val)
#
#     index = 0
#     for sublist in ordering:
#         if len(sublist) > 1:
#             subsort(sublist)
#         for val in sublist:
#             arr[index] = val
#             index += 1
#     return arr

def insertion_sort(arr:list):
    insertions = 0
    length = len(arr)
    for i in range(length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            insertions += 1
            j -= 1
        arr[j+1] = key
    return arr,insertions


# def lp_sort(arr: list) -> list:
#     return insertion_sort(linear_prediction_ranking(arr))


def linear_prediction_ranking(arr: list[Any]) -> list[Any]:
    complexity = 0
    arr_len = len(arr)
    ordering = [None for _ in range(arr_len)]
    min_val = None
    max_val = None
    ##GET MIN | MAX
    for val in arr:
        complexity += 1
        if min_val is None or min_val > val:
            min_val = val
        if max_val is None or max_val < val:
            max_val = val

    ##CALC PREDICTION FUNCTION

    if min_val == max_val:
        return arr
    if not (min_val is None or max_val is None):
        m = (-arr_len + 1) / (min_val - max_val)
        c = 0 - m * min_val

        for val in arr:
            y = m * val + c
            approx_index = int(y)
            dist = 0
            while True:
                complexity += 1
                if approx_index + dist < arr_len and ordering[approx_index + dist] is None:
                    approx_index += dist
                    break
                elif approx_index - dist >= 0 and ordering[approx_index - dist] is None:
                    approx_index -= dist
                    break
                elif approx_index - dist < 0 and approx_index + dist >= arr_len:
                    print('Error: no value position found!')
                    break
                dist += 1
            ordering[approx_index] = val

    return ordering,complexity


if __name__ == "__main__":
    test_arr = [random.randint(1,100) for i in range(10)]
    print(test_arr)
    print(lp_sort(test_arr))
