l = input()
l = l.split(' ')

operators = ['+', '-', '*', '/']
ops = []
opd = []
try:
	while 1:
		if not l:
			break
		n = l.pop(0)
		if n not in operators:
			opd.append(n)
			continue
		new_expr = eval(opd.pop(-2) + n + opd.pop())
		opd.append(str(new_expr))
	if len(opd) != 1:
		print('ERROR')
	else:
		print(opd.pop())
except:
	print('ERROR')