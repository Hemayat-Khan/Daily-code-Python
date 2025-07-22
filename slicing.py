#Slicing:it is the way to extarct a subset of data from a numpy array
import numpy as np
#---one dimensional-------#
# list1=[10,20,30,40,50,60,70]
# arr1=np.array(list1)
# print(arr1[1:3])
# print(arr1[2:4])
# print(arr1[1:6:2])
# print(arr1[-1:-3:-1])#[start,stop,step]
# print(arr1[0:3])
# print(arr1[::2])#[s,s,s] not given but only step is gievn
# print(arr1[::-1])#[s,s,s]
# print(arr1[1:-1])
# print(arr1[2::])
#---multi dimensional ------#
list2=[[1,2,3],[2,3,4],[5,6,7],[8,9,10]]
arr2=np.array(list2)
# print(arr2[1,])
# print(arr2[:,1])
# print(arr2[1:2,1:2])
# print(arr2[1:3,])
# print(arr2[1:3,1])
print(arr2[1:3,:1])
print(arr2[1:3,1:])
print(arr2[:,1:3])