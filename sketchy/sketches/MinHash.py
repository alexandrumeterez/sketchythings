from zlib import crc32

class MinHash(object):
	def __init__(self, k, m) -> None:
		self.k = k
		self.m = m

	def hash_(self, b):
		return float(crc32((str.encode(b))) & 0xffffffff) / 2**32

	def sketch(self, s):
		n = len(s)
		hashes = []
		for i in range(0, n - self.k):
			kmer = s[i:i + self.k]
			hashes.append(self.hash_(kmer))
		hashes = sorted(hashes)
		return hashes
	
	def estimate(self, data):
		return self.m * 1 / data[-1] - 1 

	def jaccard(self, s1, s2):
		s1_hashes = self.sketch(s1)
		s2_hashes = self.sketch(s2)

		s1_topm = sorted(s1_hashes)[:self.m]
		s2_topm = sorted(s2_hashes)[:self.m]

		union_sketch = sorted(list(set((s1_topm + s2_topm))))[:self.m]
		J = (self.estimate(s1_topm) + self.estimate(s2_topm) - self.estimate(union_sketch)) / self.estimate(union_sketch)
		return J