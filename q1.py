table_quartic = ['-'] * 23;
table_double = ['-'] * 23;

def h(k):
	return (4 * k + 7) % 23

def h2(k):
	return (17 - (k % 17))

def hash_double(keys):
	for k in keys:
		hk = h(k)

		if(table_double[hk] != '-'):
			hk = h2(k)

		table_double[hk] = 'X'
	return table_double


def hash_quartic(keys):
	for k in keys:
		ak = hk = h(k)
		j = 0

		while(table_quartic[ak] != '-'):
			ak = (h(k) + j**4) % 23
			j += 1

		table_quartic[ak] = 'X'
	return table_quartic