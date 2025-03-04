import numpy as np

x = [1,2,3,4]
y = [4,5,6,7]
'''
z = []
for i,j in zip(x,y):
    z.append(i+j)
'''

z = np.add(x,y)
print(z)
print(np.subtract(y, x))
print(np.multiply(y, x))
print(np.divide(y, x))
print(np.power(y, x))
print(np.mod(y, x))
print(np.divmod(y, x))
print("Sum of sum in each array: ",np.sum([x,y]))
print("Show sum in each array: ",np.sum([x,y], axis= 1))
print("Cummulative Sum: ", np.cumsum(x))

def myadd(x,y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3],[4,5,6]))
print("Function type: ", type(myadd), type(zip))

# Rounding Decimal
print(np.trunc([-3.1666, 3.6667]))
print(np.fix([-3.1666, 3.6667]))
print(np.floor([-3.1666, 3.6667]))
print(np.ceil([-3.1666, 3.6667]))
print(np.around(-3.1666, 3))

# Logarithm
print(np.log2(np.arange(1,10)))
print(np.log10(np.arange(1,10)))
print(np.log(np.arange(1,10))) # nature log - e
print(np.log1p(np.arange(1,10)))

from math import log
log_base_n = np.frompyfunc(log, 2, 1)
print(log_base_n(100, 10))

# Products
print(np.prod(x))
print(np.prod([x,y]))
print(np.prod([x,y], axis=1))
print(np.cumprod(x))
print(np.prod([x,y]))

# Trigonometric
arr = np.array([np.pi/2, np.pi/3,np.pi/4,np.pi/4,np.pi/5])
deg_arr = np.array([90, 180, 270,360])

print(np.sin(arr))
print(np.deg2rad(deg_arr))
print(np.rad2deg(arr))
print(np.arcsin(np.array([1,-1,0.1])))
print(np.hypot(3,4)) # find hypotenues
print(np.arcsinh(1.0))

# set operation
arr1 = np.array([1,2,3,4,4])
arr2 = np.array([4,5,6,7])
print(np.unique(arr1))
print(np.union1d(arr1,arr2))
print(np.intersect1d(arr1,arr2, assume_unique=True))
print(np.setdiff1d(arr1,arr2, assume_unique=True))
print(np.setxor1d(arr1,arr2, assume_unique=True))