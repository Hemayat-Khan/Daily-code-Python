#----Attributes of Numpy Array------#
import numpy as np
"""1:ndim: show dimension that it is one  or two or three dimensional
2:shape:what is the shape mean two rows and 3 columns then it is 2 by 3
3:size:let suppose we have 2 by 3 array then we have 6 elements, so it is the size 
4: dtype : it is used to show the data in different datatypes which the user want
5: itemsize:if we have int in the array then we know that the size of int is 4 byte ,it mens that it shows us the size of datatype"""
# list1=[1,2,3,4,5,6]
# arr1=np.array(list1)
# print(arr1.ndim)# output is 1 bcz it is one dimensional
# #---2 dimensional-----#
# list2=[[1,2,3],[3,4,5]]
# arr=np.array(list2)
# print(arr.ndim)# output:2
#----3 dimensional-------
# list3=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
# arr2=np.array(list3)
# print(arr2.ndim)# output: 3 dimensional
#-----shape and size,dtype,itemsize------#
#---one ----#
list1=[1.0,2.0,3.0,4.8,5.4]
arr=np.array(list1)
print("Single dimensional")
print(arr.shape)#output:7,
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
#---two dimensional-----
list2=[[1,2,3],[4,5,6]]
arr1=np.array(list2)
print("Two dimensional")
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)
#---3 dimensional-----#
list3=[[[1,2,3],[5,6,7]],[[7,8,9],[10,11,12]]]
arr3=np.array(list3)
print(arr3.ndim)
print(arr3.shape)
print(arr3.size)
print(arr3.dtype)
print(arr3.itemsize)
