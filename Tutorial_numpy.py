import numpy as np

#tuple: () chi chua mot du lieu duy nhat 
#array: []

#np. array: khoi tao mang da chieu
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# ndim: show the number of dimensions
print(a.ndim)
# Khoi tao voi so luong chieu co dinh
arr = np.array([1, 2, 3, 4], ndmin=5)

arr= np.array([1,2,3,4,5,6,7,8])
print(arr)
print("number of dimension:", arr.ndim)

#Access array ele

print(arr[0])

# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])

#Access 2-D Arrays
arr1  = np.array([[1,2,3],[4,5,6]])

print(arr1[0,1])

#Access 3-D Arrays
arr_n = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr_n[0, 0, 2])

#Negative Indexing


arr_negav = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr_negav[1, -1])

# slicing
# [start:end]
# [start:end:step]
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1


print(arr[1:5])
print(arr[2:])
print(arr[:4])
print(arr[-3:-1])

#step
print(arr[1:5:2])

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

#checking data type

print(arr.dtype)

#creating array with a defined data type

ak = np.array([1,2,3,4], dtype='S')

print(ak)
print(ak.dtype)
# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, 
# is to make a copy of the array with the astype() method.

new_ak = ak.astype(bool)

print(new_ak)

#copy vs view 
#copy sở hữu data của og, việc sửa đổi sẽ không ảnh hưởng tới og
#view ko sở hữu data của og, việc sửa đổi có ảnh hưởng tới og và ngược lại 

x = arr.copy()
y = arr.view()
# trả về mảng đang base
print(x.base)
print(y.base)

#SHAPE
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
# trả về 2,4 số chiều ma trận, với số chiều ma trận ngoài là 2, trong đó là ma trận có 4
#giải thích: xét ma trận ngoài thì có 2 thành phần, xét vào trong thì có 4 thành phần


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
# print('shape of array :', arr.shape)


#reshape 
# Unknown Dimension
# You are allowed to have one "unknown" dimension.

# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

# Pass -1 as the value, and NumPy will calculate this number for you

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# cũng có thể dùng -1 để flattening the array


# Array iterating

# Iterating Arrays Using nditer()
# dùng thay các vòng for
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

# Iterating Array With Different Data Types
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements 
# while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) 
# so it needs some other space to perform this action, that extra space is called buffer, 
# and in order to enable it in nditer() we pass flags=['buffered'].

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

for x in np.nditer(arr[:, ::2]):
  print(x)

#Enumerated Iteration Using ndenumerate()

for idx, x in np.ndenumerate(arr):
  print(idx, x)

#NumPy Joining Array


# nối
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

# nối array 2-d (axis=1)
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1) # axis=0 ghép theo chiều dọc , axis=1 ghép theo chiều ngang

print(arr)

#ghép sử dụng stack function 
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# Split array 
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
print(newarr) 
# chia ra thành ba arr trong 1 array 

#Split the 2-D array into three 2-D arrays along columns.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# Searching arrays

# where 
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
# The example above will return a tuple: (array([3, 5, 6],)

# searchsorted(): sử dụng binary search, thường dùng để chèn, trả về kết quả index để trèn, default sẽ thường
# bên trái, nhưng ta có thể chỉnh sửa 

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

# Multiple Values
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6]) # -> trả về array[1,2,3] (index)
# trả về vị trí mà các phần từ trong array sẽ chèn ở đâu

# Sort

# sử dụng sort
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# sort theo kiểu 2d, sort trong từng phần tử, vị trí trong arr chung vẫn giữ nguyên
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

# filter 
# ta gán x vào arr chỗ nào có true thì sẽ hiện còn false thì sẽ bị biến mất khỏi new arr

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# Tạo một cái lọc
# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# có thể lọc trực tiếp
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
