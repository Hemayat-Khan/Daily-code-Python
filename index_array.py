#-----indexing in Numpy Array---#
import numpy as np
list1=[10,20,30,40,50]
arr1=np.array(list1)
print(arr1[3])
print(arr1[0])
print(arr1[-1])
#---2d array---#
list2=[[1,2,3],[2,4,5],[4,5,6]]
arr2=np.array(list2)
print(arr2[0,:])#[row, column]
print(arr2[1,1])
print(arr2[:,2])
print(arr2[:,1])