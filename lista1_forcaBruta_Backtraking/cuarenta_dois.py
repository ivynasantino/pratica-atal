entrada = int(raw_input())

def op_and(it, maior, b , num1, num2):
	if(it >= b and num1 > maior):
		maior = num1
		
	for i in range(len(num2)):
		if(num1 & num2[i] > maior):
			maior = op_and(it+1, maior, b, num1 & num2[i], num2[i+1:])
			
	return maior
	
for i in range(entrada):
	lista = []
	a, b = map(int,raw_input().split())
	numeros = map(int,raw_input().split())
	
	
	for i in xrange(len(numeros)):
		lista.append(op_and(1, 0, b, numeros[i], numeros[i+1:]))
		
	print max(lista)
