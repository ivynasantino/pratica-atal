n = int(raw_input())

def fib(n):	
	seq_f = [0,1]
	calls = [0,0]
	
	for i in xrange(2, n+1):
		seq_f.append(seq_f[i-1] + seq_f[i-2])
		calls.append(calls[i-1] + calls[i-2] + 2)
	
	return seq_f[n], calls[n]
	
	
for i in xrange(n):
	f = int(raw_input())
	seq, call = fib(f)
	print "fib(%d) = %d calls = %d" % (f, call, seq)
	
