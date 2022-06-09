from tracemalloc import start
from sympy import Q
from sketches.MinHash import MinHash
from sketches.Minimap import Minimap

import random
import numpy as np
import matplotlib.pyplot as plt
random.seed(0)
def mutate(s, alphabet, rate):
	new_s = list(s)
	for i in range(len(s)):
		chance = random.random() < rate
		if chance:
			new_s[i] = np.random.choice(list(set(alphabet) - set([s[i]])), 1)[0]
	return ''.join(new_s)

if __name__ == '__main__':
	N = 10000
	RATE = 0.1
	K = 10
	alphabet = ['A', 'C', 'T', 'G']
	genome = "".join(np.random.choice(alphabet, N))
	# mutated_genome = mutate(genome, alphabet, RATE)
	# y = []
	# for k in range(10, 200):
	# 	mh = MinHash(k=k, m=500)
	# 	y.append(mh.jaccard(genome, mutated_genome))
	
	# plt.figure()
	# plt.plot(y)
	# plt.show()

	mm = Minimap(w=6, k=10)

	# get seqs from genome
	seqs = []
	for i in range(20):
		start_pos = np.random.randint(0, len(genome) - 100, 1)[0]
		seqs.append(genome[start_pos:start_pos + 100])

	H = mm.build_index(seqs)
	seq = mutate(seqs[6], alphabet, 0.25)
	A = mm.map_query(H, seq, 0.04)
	print(len(A))
	for results in A:	
		print(results)
		seq_num, strand, s, e = results
		print(results)
		i = s + e
		i_ = e

		print(seqs[seq_num])
		temp = list(" " * len(seqs[seq_num]))
		temp[i_] = "^"
		print("".join(temp))

		print(seq)
		temp = list(" " * len(seq))
		temp[i] = "^"
		print("".join(temp))	
		
		print("\n")