text = ""
s = input()
while s!="":
	s+="\n"
	text+=s
	s = input()

a = text.split('\n')
aa = []
for i in a:
	aa.extend(i.split(' '))

while True:
	try:
		aa.remove('')
	except:
		break
max_count = 0
res = '---'
for i in aa:
	if aa.count(i) > max_count:
		max_count = aa.count(i)
		res = i
	elif aa.count(i) == max_count:
		res = '---'
print(res)