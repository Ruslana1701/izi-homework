def second_max(arr):
    max_arr = max(arr)
    if arr.count(max_arr) == len(arr):
        return 'NO'
    for a in sorted(arr, reverse=True):
        if a<max_arr:
            return a
    return 'NO'

arr = list()
for a in input().split(','):
    arr.append(int(a))

print(second_max(arr))