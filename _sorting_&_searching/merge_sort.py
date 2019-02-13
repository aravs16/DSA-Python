def merge(l, r):
    print("Merging",l,r)
    merged = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged.append(l[i])
            i = i + 1
        else:
            merged.append(r[j])
            j = j + 1

    return merged+l[i:]+r[j:]

def _sort(ar):

    if len(ar) <=1:
        return ar

    l = len(ar)
    mid = l//2

    left = ar[0:mid]
    right = ar[mid:]

    ll = _sort(left)
    rr = _sort(right)

    merged =  merge(ll, rr)

    return merged


print('Sorted',_sort([7,6,5,4,3,2,1,0]))