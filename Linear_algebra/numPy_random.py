# import numpy as np 
# from numpy import random

# x= random.randint(100)
# x= random.rand()

# # generate random array

# x= random.randint(100,size=(5))
# # Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
# x = random.randint(100, size=(3, 5))

# #Generate a 2-D array with 3 rows, each row containing 5 random numbers:
# x = random.rand(3,5)

# #các phương thức cho permutation 

# arr = np.array([1, 2, 3, 4, 5])

# random.shuffle(arr) #shuffle làm thay đổi array
# random.permutation(arr) #permutation ko làm thay đổi array 

# print(arr)

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.displot([1,2,3,4,5], kind="kde")
x = random.normal(loc= 2, scale=1, size=(2, 3))
print(x)

