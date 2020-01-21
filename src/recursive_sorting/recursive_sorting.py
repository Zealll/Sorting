# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO 
    left = 0
    right = 0
    for i in range(elements):
        if left >= len(arrA):
            merged_arr[i] = arrB[right]
            right += 1
        elif right >= len(arrB):
            merged_arr[i] = arrA[left]
            left += 1
        elif arrA[left] < arrB[right]:
            merged_arr[i] = arrA[left]
            left += 1
        else:
            merged_arr[i] = arrB[right]
            right += 1
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[ :len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2: ])
        arr = merge(left, right)
      

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
