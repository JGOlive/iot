import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
#
#
#

# create a array with zeros
b = np.zeros((3,4))
print(b)

# Find the shape of the array
sh = a.shape
print("shape is:", sh)

# Find the dimension of the array
nd = a.ndim
print("ndim is:", nd)

#
sh = a.size
print("size is:", sh)

#
tp = type(a)
print("type is:", tp)

#
tpa = a.dtype
print("dtype is:", tpa)

#
su = a.sum()
print("sum is:", su)

#
mx = a.max()
print("max is:", mx)

#
#
sq = np.sqrt(a)
print("sqrt is:", sq)