from itertools import product

numbers = input()
numbers = numbers.split(' ')
complexity = len(numbers)

signs = ['+', '-']

combs = list(product(signs, repeat=complexity-2))

flag = 0

for comb in combs:
    for i, number in enumerate(numbers[:-1]):
        c = list(comb[:])
        c.insert(i, '==')
        equation = ''.join(reduce(lambda x, y: x + y, zip(numbers, c))) + numbers[-1]
        if eval(equation):
            print('YES')
            flag = 1
            break
    if flag:
        break
else:
    print('NO')
