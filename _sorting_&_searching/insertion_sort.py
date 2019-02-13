def _sort(arr):
    for i in range(1,len(arr)):
        current_val = arr[i]
        position = i
        print(i, current_val)
        for j in range(i-1,-1,-1):
            print(arr[j],'<<')
            if arr[j] > current_val:
                arr[j+1] = arr[j]
                position = position -1
            print("position", position)

        arr[position] = current_val

    return arr


print(_sort([3, 5, 1, 2, 0, 4, 6]))