des_cache = {}
fact_cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9 : 362880}

def child(i):
	s = 0
	while i:
		digit = i % 10
		s += fact_cache[digit]
		i //= 10
	return s

def strength(i, k):
	children = []
	x = child(i)
	
	while(not(x in children)):
		children.append(x)
		if(x in des_cache):
			#removing duplicates
			a = des_cache[x]
			for j in children:
				if(j in des_cache[x]):
					a = des_cache[x][0:des_cache[x].index(j)]
					break
			children = children + a
			break
		x = child(x)
	
	n = len(children)

	#caching all known subsets
	c = 0
	while(not(children[c] == x)):
		des_cache[children[c]] = children[c + 1:n]
		c += 1

	return n == k

def descendants(n1, n2, k):
	z = 0
	for i in reversed(range(n1, n2)):
		if(strength(i, k)):
			z += 1
	return z