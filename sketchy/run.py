from sketches.MinHash import MinHash
import random
import numpy as np
import matplotlib.pyplot as plt

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
	mutated_genome = mutate(genome, alphabet, RATE)
	y = []
	for k in range(10, 200):
		mh = MinHash(k=k, m=500)
		y.append(mh.jaccard(genome, mutated_genome))
	
	plt.figure()
	plt.plot(y)
	plt.show()