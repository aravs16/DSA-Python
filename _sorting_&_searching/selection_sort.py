def _sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max = 0
        for j in range(0, i):
            if arr[j] > arr[max]:
                max = j
        if arr[max] > arr[i]:
            arr[i], arr[max] = arr[max], arr[i]

    return arr

print(_sort([6,5,7,4,3,2,1]))
