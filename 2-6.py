l = input()
m,n = [for int(n) in l.split(',')]

res_len = len(str(m*n))
max_len = len(str(m)+str(n))

for i in range(1, n+1):
	res = ''

	if len(str(m*i)) < res_len:
        for j in range(0, res_len - len(str(m*i))):
            res+='_'

	res+=str(m*i)+'=_'

	if max_len > len(str(m)+str(i)):
		for j in range(0, max_len-len(str(m)+str(i))):
			res+='_'
			
	res+=str(i)+'_'+str(m)

	print(res)