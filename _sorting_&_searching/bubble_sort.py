def _sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(_sort([6,5,4,3,2,1,7]))
