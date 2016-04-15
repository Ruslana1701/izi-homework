def properties(obj): 
    for d in dir(obj):
        if d[0] is not '_':
            print(d)

    return True

properties(input())