# Building a max-heap
# 1. max-heapify method simply takes an index, compares the value at index with left child and right child.
#    Swaps the value at the index with the largest of the 3 and calls max-heapify with the index where largest value was found.
#    Note: left child of an idx = 2*idx+1 and right child = 2*idx+2
# 2. Build heap calls max-heap for every non leaf node going backwards from the first non-leaf node from bottom to the root.


def max_heapify(h_list, idx):
    l = 2*idx + 1
    r = 2*idx + 2
    largest = idx
    if l < len(h_list) and h_list[l] > h_list[largest]:
        largest = l
    if r < len(h_list) and h_list[r] > h_list[largest]:
        largest = r
    if largest != idx:
        h_list[idx], h_list[largest] = h_list[largest], h_list[idx]
        max_heapify(h_list, largest)

def build_heap(h_l):
    first_non_leaf = (len(h_l)//2)-1
    for m in range(first_non_leaf,-1,-1):
        max_heapify(h_l,m)
    return h_l

def del_root(h_l):
    h_l[0],h_l[-1 ]= h_l[-1],h_l[0]
    max_heapify(h_l,0)
    h_l.pop()

def insert(h_l,x):
    h_l.append(x)
    idx = len(h_l)-1
    while True:
        parent = (idx-1)//2
        if parent >=0 and h_l[parent] < h_l[idx]:
            print("Swapping",h_l[parent],h_l[idx])
            h_l[parent], h_l[idx] = h_l[idx], h_l[parent]
            idx = parent
        else:
            break


h_l = [1,2,3,4,5,6,7,8,9]
build_heap(h_l)
print(h_l)
del_root(h_l)
print(h_l)
insert(h_l,10)
print(h_l)


