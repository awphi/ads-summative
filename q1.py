def h(k):
	return (4 * k + 7) % 23

def h2(k):
	return 17 - (k % 17)

def hash_double(keys):
	table_double = ['-'] * 23;
	for k in keys:
		ak = hk = h(k)
		h2k = h2(k)
		j = 0

		while(table_double[ak] != '-'):
			ak = (hk + (j * h2k)) % 23
			j += 1

		table_double[ak] = k
	return table_double


def hash_quartic(keys):
	table_quartic = ['-'] * 23;
	for k in keys:
		ak = hk = h(k)
		j = 0

		while(table_quartic[ak] != '-' and '-' in table_quartic):
			ak = (h(k) + j**4) % 23
			j += 1

		table_quartic[ak] = k
	return table_quartic