from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100, size=(5))
y = random.randint(100, size=(3,5))

f = random.rand(5)
print(x)
print(y)
print(f)

# generate random number from array
print(random.choice([1,2,3,4,5,6]))
print(random.randint(100, size=(5)))
print(random.rand(3,5))
print(random.choice([1,2,3,4,5,6],size=(3,5)))

# random distribution
print(random.choice([1,2,3,4,5,6], size=(100), p=[0.1, .3, .2, .3, .1, 0]))
print(random.choice([1,2,3,4,5,6], size=(3,2), p=[0.1, .3, .2, .3, .1, 0]))

# shuffling/ permutation of array
arr = np.array([1,2,3,4,5,6])
print(random.permutation(arr))
print(arr)
random.shuffle(arr) #change original arr
print(arr)

# seaborn module
# sns.distplot(arr,hist=False)
# plt.show()

print(random.normal(loc=1, scale=2, size=(2,3)))

# sns.distplot(random.normal(size=1000), hist=False)

# plt.show()

print(random.binomial(n=10, p=.5, size=5))

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

# plt.show()

print(random.poisson(lam=2, size=10))
print(random.uniform(size=(2,3)))

print(random.logistic(loc=1, scale=2, size=(2,3)))

# Multinomial Distribution
print(random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6]))#dice roll

# Exponential Distribution
print(random.exponential(scale=2, size=(2,3)))

# Chi Square Distribution
print(random.chisquare(df=2, size=(2,3)))

# Rayleigh Distribution
print(random.rayleigh(scale=2, size=(2,3)))

# Pareto Distribution
print(random.pareto(a=2, size=(2,3)))