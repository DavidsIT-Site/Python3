# performing matrix array stuff


import numpy as np
m = np.matrix([[1, -2, 3], [0, 3, 5], [7, 8, -9]])
print("{}    {}     {}".format(m, m.T, m.I))


#named tuple??
vector = np.matrix([[2], [3], [4]])
print(vector)

import numpy.linalg

print('{}        {}'.format(numpy.linalg.det(m), numpy.linalg.eigvals(m)))

solutions = numpy.linalg.solve(m, vector)
print(solutions)
tmp = m*solutions
print(tmp)
print(vector)
