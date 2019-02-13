def _sort(arr):
    l = len(arr)
    if l <= 1:
        return arr
    pivot = arr[l-1]
    r = q = 0

    while r < l-1:
        if arr[r] < pivot:
            arr[q],arr[r] = arr[r],arr[q]
            q = q + 1
        r = r + 1

    arr[l-1], arr[q] = arr[q], arr[l-1]

    left = _sort(arr[0:q])
    right = _sort(arr[q+1:])

    return left+[arr[q]]+right

print(_sort([6,5,4,3,2,1,0]))