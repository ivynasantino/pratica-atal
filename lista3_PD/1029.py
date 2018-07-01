n = int(raw_input())
cont = -1

def fib(num):
	global cont
	cont += 1
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num-1) + fib(num-2)
		
for i in xrange(n):
	f = int(raw_input())
	calc = fib(f)
	print "fib(%d) = %d calls = %d" % (f, cont, calc)
	cont = -1 
