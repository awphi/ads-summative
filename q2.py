des_cache = {}
fact_cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9 : 362880}

def child(i):
	s = 0
	while i:
		digit = i % 10
		s += fact_cache[digit]
		i //= 10
	return s

def strength(i):
	children = []
	x = child(i)
	while(not(x in children)):
		children.append(x)
		if(x in des_cache):
			children = list(set(children + des_cache[x]))
			break
		x = child(x)
	des_cache[i] = children
	return len(children)

def descendants(n1, n2, k):
	z = 0
	for i in range(n1, n2):
		if(strength(i) == k):
			z += 1
	return z
