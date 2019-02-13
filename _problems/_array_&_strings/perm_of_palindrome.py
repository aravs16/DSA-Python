def _pp(str):
    a={}
    for i in str:
        if i in a:
            a[i] = a[i]-1
        else:
            a[i] = 1

    count = 0
    for i in a:
        if a[i]%2 != 0:
            count = count+1

    
    return count == 1 or count == 0


print(_pp("tactcoaa"))
