import numpy as np
from numpy.random import rand
from numpy.linalg import solve, inv

a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
b = a.transpose()
print(b)

b = inv(a)
print(b)

b = np.array([3, 2, 1])
c = solve(a, b) # solve the equation ax = b
print(c)
print()

c = rand(3, 3) * 20 # create a 3x3 random matrix of values 
print(c)

d = np.dot(a, c) # matrix multiplication
print(d)

d = a @ c # Starting with Python 3.5 and NumPy 1.10
print(d)

#push