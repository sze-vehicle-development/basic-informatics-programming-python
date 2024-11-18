def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))
arr = [12, 11, 13, 5, 6]
print(merge_sort(arr))