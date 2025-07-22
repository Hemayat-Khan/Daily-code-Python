#----Arthmetic operation on Numpy-----
#--Addition----#
import numpy as np
list1=[[1,2,3],[3,4,5]]
list2=[[4,5,6],[7,8,9]]
x=np.array(list1)
y=np.array(list2)
z= x+y
print(z)
#---Subtraction
z= y-x#or x-y it is same
print(z)
#---Multiplication----
z= x*y
print(z)
#----matrix multiplication-----#
# z= x @ y
# print(z)# it is not perform on the given matrix bcz if we multiple the row with column then it as one value remaining.
list3=[[1,2],[2,3]]
list4=[[2,4],[4,5]]# Example:
a=np.array(list3)#[a b]   [w x]  ,[aw +by    ax + bz]      
b=np.array(list4)#[c  d]  [y z],   [cw +dy    cx + dz]
z= a @ b
print(z)
#----Division---
z= b/ a
print(z)
#---floor division----#
#in this floor value is ignore mean flaot value is not included
z= b//a
print(z)
#---exponention----
z= y ** x
print(z)
#----Modulo:  it mean remainder---
z= y % x
print(z)