
import numpy as np

#list working

#list_a=[1,2,3,4]
#list_b=[5,6,7,8]

#print(list_a*list_b)

#numpy_a=np.array([1,2,3,4])
#numpy_b=np.array([5,6,7,8])
#print(numpy_a)
#print(numpy_a*numpy_b)

#common properties

numpyBasics_array=np.array([1,2,3,4,10.53,"u"])

print(numpyBasics_array.dtype)
print(numpyBasics_array.itemsize)
print(numpyBasics_array.size)

#2D arrays

array_2D=np.array([[1,2,3],[3,4,5],[6,7,8]])
array_2D=np.array([[5*2,3*2,1*4],[2*7,2*3,1*3],[1*4,3*2,3*2]])
print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("Shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))

array_2D=np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)

#accessing arrays

array_x=np.array([[1,2,3,4],[5,6,7,8]])
print(array_x)
print(array_x.size)

print(array_x[1,2])
print(array_x[0,2])
print(array_x[: ,2])
print(array_x[: ,-3])

#step - start:end:stepsize

print(array_x[0, 0:4:2])

print(array_x[:, 0:4:2])

#3D arrays

array_3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array_3d)
print(array_3d[0,1,0])
print("************")
print(array_3d[1])
print("***************")
array_3d[:,0,:]=100
print(array_3d.shape)
array_3d[0,0]=[2,4]
print(array_3d)

array_3d[:,0,:]=[[12,13],[14,15]]
print(array_3d)

#common arrays
#one's two's empty

print(np.zeros(3))


print(np.ones(3))

two_d=np.zeros((3,3))
print(two_d)

three_d=np.zeros((2,3,3))
print(three_d)

four_d=np.zeros((2,3,3,2))
print(four_d)

print(np.full((3,3),[1,2,3],dtype='float32'))

array_r=[[1,2,3],[4,5,6]]

array_repeat=np.repeat(array_r,2,axis=0)

print(array_repeat)

array_zeros=np.zeros((3,3))
array_zeros[1,1]=7
print(array_zeros)

update_array=np.zeros((5,5))
update_array[1:-1,1:-1]=array_zeros
print(update_array)



array_zeros=np.zeros((5,5),dtype='int32')
array_zeros[2,2]=7
print(array_zeros)

update_array=np.zeros((7,7),dtype='int32')
update_array[1:-1,1:-1]=array_zeros
print(update_array)

#math operations

array_math=np.array([1,2,3])

print("Declare array: {}".format((array_math)))
print("Add 10 to array: {}".format(array_math+10))
print("Sub 10 from array: {}".format(array_math-10))
print("Raise to pow array: {}".format(array_math**3))
print("Mul with array: {}".format(array_math*5))
print("div to array. {}".format(array_math/2))
print(np.sin(array_math))
print(np.cos(array_math))
print(np.size(array_math))

arr_a=np.ones((2,3),dtype='int32')
arr_b=np.full((3,2), 2,dtype='int32')

print(np.matmul(arr_a,arr_b))

print(np.matmul(arr_b,arr_a))

#statistics

n_a=[[1,1,1,1],[0,0,0,0,0,0]]

print(n_a)

array_stats=[[1,2,3],[-1,3,0],[4,5,-6]]

print(np.min(array_stats))
print(np.min(array_stats,axis=0))
print(np.min(array_stats,axis=1))

print(np.max(array_stats))
print(np.max(array_stats,axis=0))
print(np.max(array_stats,axis=1))

print(np.sum(array_stats))


#reshape

four_D=np.arange(36).reshape(2,3,3,2)
print(four_D)

# arange - array range

one_d=np.arange(6)
print(one_d)

array_one=np.array([10,20,30,40])
array_two=np.arange(10,50,10)
print(array_one*array_two)
print(array_one@array_two)
print(array_one.dot(array_two))

a=np.array((1,2,3))
b=np.array((4,5,6))

c=np.hstack((a,b))
print(c)

a=np.array([[1],[2],[3]])
b=np.array([[4],[5],[6]])
c=np.hstack((a,b))
print(c)











####################################################################3

data_from_text_file=np.genfromtxt('numpy.txt',dtype='int32',delimiter=',')
print(data_from_text_file)
print(data_from_text_file>10)

#advance indexing
print(data_from_text_file[data_from_text_file>10])

print(data_from_text_file*2)

#fill values
print("@@@@@@@@@@@@@@@@@@@")
fill_values=np.genfromtxt('numpy.txt',delimiter=',',dtype='int32',filling_values=100)
print(fill_values)
print(data_from_text_file)
print("@@@@@@@@@@@@@@@@@@@@")


def numpy_function(x,y):
    return 10*x+y
b=np.fromfunction(numpy_function,(2,3),dtype='int32')
print(b)

def numpy_function(x,y,z):
    return 10* x+ y-z
b=np.fromfunction(numpy_function,(3,4,2),dtype='int32')
print(b)


