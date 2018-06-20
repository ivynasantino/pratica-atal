
while True:
	n = int(raw_input())
	if n == 0: break
	inp = map(int, raw_input().split())
	
	
	soma = 0
	for i in range(1, len(inp)):
		soma += abs(inp[i-1])
		inp[i] += inp[i-1]
			
	print soma
