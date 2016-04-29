from collections import defaultdict

costs = [int(x) for x in input().split(', ')]
step = int(input())

mins = defaultdict(list)
def paid_stairs(costs):
	if not costs:
		return 0
	if len(costs) == 1:
		return costs[0]
	for s in range(step):
		mins[s].append(paid_stairs(costs[:-s-1]))
	m = [i.pop() for i in mins.values() if i]
	return costs[-1] + min(m)

if len(costs) <= step:
	print(costs[-1])
else:
	print(paid_stairs(costs))