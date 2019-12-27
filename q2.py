des_cache = {}
fact_cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9 : 362880}

def child(i):
	s = 0
	while i:
		digit = i % 10
		s += fact_cache[digit]
		i //= 10
	return s

#maybe sort the number (like a string) and cache/recall from the cache with that?
def strength(i, k):
	children = []
	x = child(i)
	while(not(x in children)):
		children.append(x)
		if(x in des_cache):
			a = des_cache[x]
			for j in children:
				if(j in des_cache[x]):
					a = des_cache[x][0:des_cache[x].index(j)]
					break
			children = children + a
			break
		x = child(x)

	idx = children.index(x)
	n = len(children)

	for j in reversed(range(0, idx)):
		des_cache[children[j]] = children[j + 1:n]

	des_cache[i] = children

	return n == k

def descendants(n1, n2, k):
	z = 0
	for i in reversed(range(n1, n2)):
		if(strength(i, k)):
			z += 1
	return z