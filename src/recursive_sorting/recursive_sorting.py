# # ======= Quick Sort By Brady! =======
# def quicksort(arr):
#     return quicksort_helper(arr, 0, len(arr))
# ​
# def quicksort_helper(arr, low, high):
#     # 1. Pick a pivot and move it until everything
#     # on the left is smaller & everything on the right is greater
#     if low >= high:
#         return
#     pivot_index = high - 1
#     for i in range(high - 1, low - 1, -1):
#         if arr[pivot_index] < arr[i]:
#             # do double swap
#             arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
#             arr[i], arr[pivot_index - 1] = arr[pivot_index - 1], arr[i]
#             pivot_index -= 1
#     quicksort_helper(arr, low, pivot_index)
#     quicksort_helper(arr, pivot_index + 1, high)


# # Original Solition
# # TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO 
#     left = 0
#     right = 0
#     for i in range(elements):
#         if left >= len(arrA):
#             merged_arr[i] = arrB[right]
#             right += 1
#         elif right >= len(arrB):
#             merged_arr[i] = arrA[left]
#             left += 1
#         elif arrA[left] < arrB[right]:
#             merged_arr[i] = arrA[left]
#             left += 1
#         else:
#             merged_arr[i] = arrB[right]
#             right += 1
#     return merged_arr



# # Original Solution
# # TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     # TO-DO
#     if len(arr) > 1:
#         left = merge_sort(arr[ :len(arr) // 2])
#         right = merge_sort(arr[len(arr) // 2: ])
#         arr = merge(left, right)
      

#     return arr


# ======== Merge Sort Improved ==========
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        print(arrB)
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
        else:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
    # merged_arr.concat(arrA)
    # merged_arr.concat(arrB)
    # return [x,y,z for x in merged_arr for y in arrA for z in arrB]

def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        return merge(merge_sort(arr[ : len(arr) // 2]), merge_sort(arr[len(arr) // 2 : ] ))
    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr1))
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
