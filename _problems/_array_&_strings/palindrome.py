def _p(str):
    start = 0
    end = len(str)-1

    while start < end:
        if str[start] == str[end]:
            start = start+1
            end = end-1
        else:
            return False

    return True


print(_p("aravkzvara"))