def _urlify(str):
    i = 0
    max = len(str)
    while i < max:
        print(str[i]==' ')
        if str[i] == ' ':
            str = str[0:i] + '%20' + str[i+1:]
            i = i + 3
            max = len(str)
            print(i, str, max)
        else:
            i = i+1

    return str


print(_urlify("This is aravind"))