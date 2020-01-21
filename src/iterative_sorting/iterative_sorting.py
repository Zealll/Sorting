# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j] :
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr1))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for _ in arr:
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    index = {}
    for i in range(10):
        index[i] = []
    
    for i in range(len(arr)):
        string = str(arr[i])
        for string_index in range(0, len(string)):
            for obj_index in index:
                print(obj_index)
                if int(string[string_index]) == obj_index:
                    index[obj_index].append(string) 
    arr = []
    for i in index:
        for j in index[i]:
            arr.append(int(j))
    return arr

print(count_sort([1, 5, 8, 4, 62, 9, 6, 0, 3, 7]))