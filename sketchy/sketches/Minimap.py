from email.policy import default
import numpy as np
from .utils import reverse_complement
from collections import defaultdict

class Minimap(object):
	def __init__(self, w, k) -> None:
		self.w = w
		self.k = k
		self.score = {
			'A': 0,
			'C': 1,
			'G': 2,
			'T': 3
		}

	def hash_(self, s):
		score = self.score
		h = 0
		k = len(s)

		for i in range(0, k):
			h += score[s[i]] * np.power(4, k - i - 1)
		return h

	def sketch(self, s):
		M = []
		w = self.w
		k = self.k
		s_rc = reverse_complement(s)
		for i in range(0, len(s) - w - k):
			m = np.inf
			for j in range(0, w - 1):
				u, v = self.hash_(s[i+j:i+j+k]), self.hash_(s_rc[i+j:i+j+k]) 
				if u != v:
					m = min(m, min(u, v))
			for j in range(0, w - 1):
				u, v = self.hash_(s[i+j:i+j+k]), self.hash_(s_rc[i+j:i+j+k]) 
				if u < v and u == m:
					M.append((m, i + j, 0))
				elif v < u and v == m:
					M.append((m, i + j, 1))
		return list(set(M))

	def build_index(self, T):
		H = defaultdict(list)
		for t in range(0, len(T)):
			M = self.sketch(T[t])
			for (h, i, r) in M:
				H[h].append((t, i, r))
		return H
	
	def map_query(self, H, q, eps):
		w = self.w
		k = self.k
		A = []
		M = self.sketch(q)

		for (h, i, r) in M:
			for (t, i_, r_) in H[h]:
				if r == r_:
					A.append((t, 0, i - i_, i_))
				else:
					A.append((t, 1, i + i_, i_))
		return A