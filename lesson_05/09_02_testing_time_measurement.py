import time

def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list
    middle = len(input_list) // 2
    left = input_list[:middle]
    right = input_list[middle:]
    left = mergesort(left)
    right = mergesort(right)
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

input_list = [12, 11, 13, 5, 6, 7]


start_time = time.time_ns()
sorted_list = mergesort(input_list)
end_time = time.time_ns()
print("Execution Time:", end_time - start_time)
print(sorted_list)
