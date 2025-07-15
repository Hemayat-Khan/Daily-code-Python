# # #----list and tuple-----
# marks=[12.3,45.6,88,"Hemayat"]
# print(marks)
# marks[3]="Khan"# the output will be [12.3,45.6,88,Khan] because list is mutable while string will give error in this case
# print(marks)
# movies=[]
# movie1=str(input("Enter first movie:")).strip().capitalize()
# movie2=str(input("Enter second movie:")).strip().capitalize()
# movie3=str(input("Enter third movie")).strip().capitalize()
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)
# # #list: it is a built in datatype that store different elements of different datatypes
# mix=[1,2.3,'khan',10]
# print(mix)
# print(type(mix))# show the type :class list
# print(len(mix))#lenght of list
# print(mix[0])
# print(mix[1])
# print(mix[2])# present a data in array
# mix[3]="King"# in list we can replace a data with other but in string we will get error
# print(mix[3])
# #----list slicing----#
# #list slicing is used to find the value in which place or we can also say it sub list
# max=[1,2,3,4,5,6,7]
# print(max)
# print(max[1:4])#start from 1 index and end on 3 index because 4 is not include
# print(max[:4])#start from 0 and end on 3
# print(max[4:])#start from 4 and end on the last elemnt of list
# #------Negative index finding---------
# print(max[-4:-1])# start from -4 and end on -2 because -1 is not include
# print(max[-5:])# start from 4 and end on 7 accordindg to the given list
# print(max[:-1])#only -1 will be not included and all other will be included
# #-------Methods of list---------#
# #---1---Append----#
# list=[1,2,3,4]
# list.append(5)# it is used to add the value in a list
# print(list)
# #----2---Sorting---#
# #-i--Ascending------#
# list1=[2,3,5,1,4,6]
# list1.sort()# it is used to come first short value
# print(list)
# #---ii-----Descending------#
# print(list1.sort(reverse=True))# it will return None
# print(list1)#Now it will print the desecending order of list
# fruits=["Apple","Banana","Mango"]
# print(fruits.sort(reverse=True))
# print(fruits)
# #---3--reverse----#
# #reverse: it is used to reverse the list#
# num=[1,2,3,4]
# num.reverse()
# print(num)# output:4,3,2,1
# #--4---Insert------#
# num1=[2,3,5,6]
# num1.insert(0,1)
# print(num1)# output:1,2,3,5,6
# #--5----remove-----
# #remove: it remove the value from the list
# list3=["Hemayat","Khan","is","No","More"]
# list3.remove("No")#No will be remove from the list
# print(list3)
# #---6---Pop------#
# # Pop: it work on index and delete the value on the base of index
# Num=["Aurangzeb","Kaif","Amaid","Hemayat"]
# Num.pop(1)
# print(Num)
# #-------------------------------------------------------------------------------#
# # ------Tuple---------#
# #Tuple: A built in datatype which is immutable#
# tup=(1,2,3,3,4)
# print(tup)
# print(type(tup))
# #-----Slicing------#
# print(tup[1:4])# output:2,3,3
# print(tup[:4])# output:1,2,3,3
# print(tup[3:])# output:3,4
# #------Negative index-----#
# print(tup[-3:-1])# output:3,3
# print(tup[-4:-2])# output:2,3
# #-------Methods---------#
# #---index----#
# #index:if we want to see that where is the value stored and on which index
# print(tup.index(3))
# print(tup.index(1))
# tup1=("Mango","Banana","Lithchee")
# print(tup.index(4))
# print(tup.index(2))
# print(tup1.index("Mango"))
# #------count function-------#
# # count:this method tell us about that how many times the value is in the tuple
# tup3=(2,4,6,8,3,4,5)
# print(tup3.count(4))
# print(tup3.count(2))
# print(tup3.count(5))
# print(tup3.count(8))
# print(tup3.count(3))
# print(tup3.count(6))
#---finding palindrom in a code----#
l1=[1,2,1]#palindrom mean that if we read it from start and end then it wull be same.
l2=[1,2,3]
l1_copy=l1.copy()
l1_copy.reverse()
l2_copy=l2.copy()
l2_copy.reverse()
# if(l1_copy== l1):
#     print("palindrom")
# else:
#     print("Not palindrom")
if(l2_copy== l2):
    print("Palindrome")
else:
    print("Not palindrome")
    #---count practice-----
    tup4=("A","D","C","A","B")# we ahve to count the "A" grade in the tuple
    print(tup4.count("A"))
    #----task to sort the given list ----#
    list_2=["A","D","B","C","A","B","D","C"]
    print(list_2.sort())
    print(list_2)