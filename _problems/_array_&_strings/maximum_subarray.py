def _max_sub(arr):
    sum = -999999
    for i in range(len(arr)):
        k = 0
        for j in range(i, len(arr)):
            k = k + arr[j]
        if k > sum:
            sum = k

    return sum

# print(_max_sub([i for i in range(10000)]))


def _dyn(arr):
    k = sum = arr[0]
    for i in range(1, len(arr)):
        sum = max(arr[i], sum+arr[i])
        
        if sum > k:
            k = sum

    
    return k

# print(_dyn([i for i in range(10000)]))
print(_dyn([5,2,-3,4]))


