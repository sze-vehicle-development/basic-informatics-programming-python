def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return (quick_sort(less)
                + [pivot]
                + quick_sort(greater))

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))
arr = [12, 11, 13, 5, 6]
print(quick_sort(arr))
arr = [2, 3, 4, 10, 40]
print(quick_sort(arr))