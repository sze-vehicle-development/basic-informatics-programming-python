def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test the function
arr = [2, 3, 4, 10, 40]
target = 10
res = binary_search(arr, target)
if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array: ", str(res))