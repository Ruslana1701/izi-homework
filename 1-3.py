arr = list()
for a in input().split(','):
	arr.append(int(a))

if len(arr) > 8:
	print('Значений больше 8!')
	exit()
elif len(arr) < 8:
	print('Значений меньше 8!')
	exit()

a = (arr[3]-arr[1])/(arr[2]-arr[0])
b = (arr[7]-arr[5])/(arr[6]-arr[4])

if a == b:
	print('YES')
else:
	print('NO')