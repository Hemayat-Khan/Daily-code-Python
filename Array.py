import numpy as np # we have taken np as alice of numpy 
# list1=[1,2,3,4,5]
# arr=np.array(list1)
# print(arr)
# print(type(arr))
# list2=[  98.78,"Hemayat",94.5,90,'A'] #it will give string in the output bcz string has high level
# arr1=np.array(list2,dtype=str) # dtype is used that in which datatype you want a data.#
# print(arr1)
# #------Two dimensional Array-----------#
# list3=[[1,2,3],[4,5,6],[7,8,9]]
# arr2=np.array(list3)
# print(arr2)
#---creaating Array using range function-----#
#---single Array------
# arr1=np.arange(1,8)
# print(arr1)
# #-----Two or three dimensional Array using range function-----#
# arr2=np.arange(1,7).reshape((2,3))# in this line range has 1 to 7 but it will put only 1 to 6 and in reshape funct 2,3 it means that we have 2 rows and 3 columns
# print(arr2)
#-----creating array of zero of single and two dimensional#
arr3=np.zeros(9)
print(arr3)
#----two dimensional array of zero----#
arr3=np.zeros((2,3))
print(arr3)
#----creating array of 1 single and dimentional---#
arr3=np.ones(4)
print(arr3)


