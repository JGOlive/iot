import numpy as np
x = np.array([1, 2, 3])
print(x)

y = np.arange(10) # like Python's range, but returns an array
print(y)

a = np.array([1, 2, 3, 6])

b = np.linspace(0, 2, 4) # create an array with four equally spaced points starting with 0 and ending with 2.
print(b)

c = a-b
print(c)

d = np.linspace(-np.pi, np.pi, 100)
e = np.sin(a)
f = np.cos(a)