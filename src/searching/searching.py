# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    print(i)
    if arr[i] == target:
      return i
  return -1   # not found

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
linear_search(arr1, 6)

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while target >= arr[low]:
    mid = (low + high) // 2
    if target > arr[mid]:
      low = mid
    elif target < arr[mid]:
      high = mid
    else:
      return mid
  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if target >= arr[low]:
    if target > arr[middle]:
      return binary_search_recursive(arr, target, middle, high)
    elif target < arr[middle]:
      return binary_search_recursive(arr, target, low, middle)
    else:
      return middle
  else:
    return -1
