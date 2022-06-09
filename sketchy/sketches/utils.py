def reverse_complement(s):
	rc = []
	n = len(s)
	rc_map = {
		'A': 'T',
		'C': 'G',
		'T': 'A',
		'G': 'C'
	}
	for i in range(n - 1, 0, -1):
		rc.append(rc_map[s[i]])
	return rc
