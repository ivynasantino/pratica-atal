n = int(raw_input())
cont = -1

seq_f = []
calls = []

seq_f.append(0)
seq_f.append(1)

print seq_f
def fib(n):
	global cont
	for i in xrange(2, n):
		seq_f[i] = seq_f[i-1] + seq_f[i-2]
		cont += 1
	
	
for i in xrange(n):
	f = int(raw_input())
	calc = fib(f)
	print "fib(%d) = %d calls = %d" % (f, cont, calc)
	cont = -1 
