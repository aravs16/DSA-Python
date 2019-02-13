def _binary_search(arr, k):

    start = 0
    end = len(arr)-1

    arr.sort()

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == k:
            return True
        else:
            if k > arr[mid]:
                start = mid+1
            else:
                end = mid-1

    return False


print(_binary_search([6,2,-9,3,9,0,2],4))