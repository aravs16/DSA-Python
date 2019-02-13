def left_array_rot(arr):

    for i in range(0,len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1

    return arr

def reversal_algo_array_rot(arr, k):

    l = len(arr)

    if k > l:
        k = k%l

    start = 0
    end = k-1

    reverse_array(arr, 0, k-1)
    reverse_array(arr, k, l-1)
    reverse_array(arr, 0, l-1)

    return arr


print(reversal_algo_array_rot([1,2,3,4,5],2))

arr = [1,2,3,4,5]

print(left_array_rot(arr))
print(left_array_rot(arr))
# print(reverse_array([1]))

