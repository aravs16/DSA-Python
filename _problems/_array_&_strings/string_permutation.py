def perm_(str1, str2):
    a = {}
    for i in str1:
        if i in a:
            a[i] = a[i]+1
        else:
            a[i] = 1

    for i in str2:
        if i in a:
            a[i] = a[i] - 1
        else:
            return False

    for i in a:
        if a[i] != 0:
            return False

    return True


print(perm_("aaravindbcd", "dnivabcdara"))