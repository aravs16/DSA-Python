# https://leetcode.com/problems/first-missing-positive/submissions/

def min_heapify(h, idx):
    l = 2*idx+1
    r = 2*idx+2

    smallest = idx

    if l<len(h) and h[l]<h[smallest]:
        smallest = l
    if r<len(h) and h[r]<h[smallest]:
        smallest = r

    if smallest != idx:
        h[smallest],h[idx] = h[idx],h[smallest]
        min_heapify(h, smallest)


def build_heap(h):
    fnl = (len(h)//2)-1
    for i in range(fnl,-1,-1):
        min_heapify(h,i)
    return h

def del_root(h):
    h[0],h[-1]=h[-1],h[0]
    min_el = h.pop()
    min_heapify(h,0)
    return min_el


def find_(h):
    build_heap(h)
    k=1
    prev = None
    while len(h)!=0:
        m = del_root(h)
        if m == prev or m<1:
            pass
        else:
            prev = m
            if m == k:
                k = k+1
            else:
                return k
           
    return k

heap = [-1-3,4,5,0,1]
print(find_(heap))






