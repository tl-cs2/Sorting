# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


print('Merge function: ', merge([1, 3, 5, 7, 9], [2, 4, 6, 8]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # While your data set contains more than one item, split it in half
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[0:mid])
        right_half = merge_sort(arr[mid:])

        arr = merge(left_half, right_half)

    return arr


print('Merge sort: ', merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
