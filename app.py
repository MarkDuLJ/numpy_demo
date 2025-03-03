import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])

arr_3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

print(arr[1] + arr[2])
print(arr_2d[0,1])
print("print last element from 2nd dim:",arr_2d[0, -1])
print(arr_3d[1:])
print(arr_3d[:1])
print(arr[::2])
print(arr_2d[1,1:3])
print(arr.dtype)

str_arr = np.array([1,2,3], dtype='S')
i4_arr = np.array([1,2,3], dtype='i4')
print(str_arr.dtype)
print(i4_arr.dtype)

b_arr = np.array([-1,0,1]).astype(bool)
print(b_arr)

view_arr = arr.view()
copy_arr = arr.copy()
copy_arr[-1] = 100
print(arr, copy_arr)
print("veiw_arr is owned by: ", view_arr.base)
print("copy_arr is owned by:", copy_arr.base)
print("shape of arr_2d: ", arr_2d.shape)
print("shape of arr_3d: ", arr_3d.shape)

ndmin_arr = np.array([1,2,3,4], ndmin=5)
print("shape of ndmin_arr: ", ndmin_arr.shape)
print(ndmin_arr)

reshape_arr = arr.reshape(3,1,3)
print(reshape_arr)
print(reshape_arr.base)

flat_arr = np.array([[1,2,3],[4,5,6]]).reshape(-1)
print(flat_arr)

single_parm_arr = np.array([[1, 2, 3], [4, 5, 6]]).reshape(6)

print(single_parm_arr)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

arr_2d_2 = np.array([[11,12,13,14,15],[16,17,18,19,20]])
print(np.concatenate((arr_2d,arr_2d_2), axis=0))
print(np.concatenate((arr_2d,arr_2d_2), axis=1))

print(np.stack((arr,np.array([11,12,13,14,15,16,17,18,19])), axis=1))
print(np.hstack((arr,np.array([11,12,13,14,15,16,17,18,19]))))
print(np.vstack((arr,np.array([11,12,13,14,15,16,17,18,19]))))
print(np.dstack((arr,np.array([11,12,13,14,15,16,17,18,19]))))

print(np.array_split(arr,4))
print(np.array_split(arr_2d,2))

# find the indexes where value 7 should be inserted
print(np.searchsorted(arr,7))

print(np.sort(np.array([True,False, True])))

print(np.sort(arr_2d))

bool_filter = [True, False, True, False, True, True, True, False, False]
value_filter = arr > 5
print(arr[bool_filter])
print(arr[value_filter])