#----For loop------
# it is used for sequential traversal mean first will come 0 then 1and 2
list=[1,2,4]
list1=["Apple","banana","Mango"]
for i in list1:
    print(i)
    #--print a tuple
tup={1,2,3,4,5}
for i in tup:
    print(i)
else:
    print("loop ended")
str="Hemayat"
for char in str:
    if char == "y":
        print("y founded")
        break
    print(char)
print("Loop ended")
#---task 1----
L=[1,4,9,16,36,49,64,81,100]
for val in L:
    print(val)
#--taks2--
#finding a number by  the help of for loop
x= 36
i= 0
for val in L:
    if val == x:
        print("Founded at index:", i)
        break
    else:
        print("finding..")
    i += 1
str="Hemayat"
idx= 0
for char in str:
    if char == "y":
        print("y founded at index:", idx)
        break
    idx += 1
for str in range(0,6):
    print(str)
    
    # Print characters of the string using range and indexing
str= "Hemayat"
for i in range(len(str)):
    print(str[i])
   #finding a character in string
    str1= "Hemayat"
for i in range(len(str1)):
    if str1[i] == "y":
        print("y founded at index:", i)
        break
sum of number by for loop
n=6
sum=0
for i in range(1,n+1):
    sum+=i
    print("Total sum =",sum)
    
