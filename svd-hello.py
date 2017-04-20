import numpy as np
la = np.linalg
words = ['I', 'like', 'enjoy', 'deep', 'learning', 'NLP', 'flying', '.']
X = np.array([[0,2,1,0,0,0,0,0],
			  [2,0,0,1,0,1,0,0],
			  [1,0,0,0,0,0,1,0],
			  [0,1,0,0,1,0,0,0],
			  [0,0,0,1,0,0,0,1],
			  [0,1,0,0,0,0,0,1],
			  [0,0,1,0,0,0,0,1],
			  [0,0,0,0,1,1,1,0]
	])

U, s, Vh = la.svd(X, full_matrices=False)

print 'U'
print U
print 's'
print s
print 'Vh'
print Vh

import matplotlib as plt

for i in xrange(len(words)):
	plt.text(U[i,0], U[i,1], words[i])

