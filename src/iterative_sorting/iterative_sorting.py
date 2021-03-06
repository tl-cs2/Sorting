# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(cur_index, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        # TO-DO: swap
        # temp = smallest_index
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


print('Selection sort: ', selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for n in range(i+1, len(arr)):
            if arr[i] > arr[n]:
                temp = arr[i]
                arr[i] = arr[n]
                arr[n] = temp

    return arr


print('Bubble sort: ', bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
