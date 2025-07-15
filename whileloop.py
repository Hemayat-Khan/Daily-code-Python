#-----loop-----
# #while loop----
# count= 1
# while count<=5:
#     print("Hello")
#     count += 1

# i= 1
# while i<=5:
#    print("Hemayat",i)
#    i +=1

# print("loop ended")
# #--reverse----
# i= 5
# while i >= 0:
#     print("Hi",i)
#     i -=1

# print("loop end ")
#---task of while loop---#
#1----Print No 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i +=1
# print("loop end")
#--2----print 100 to 1----
# i= 100
# while i>=1:
#     print(i)
#     i-=1
# print("loop end")
#multiplication----
# i= 1
# n=int(input("Enter your number:"))
# while i<=10:
#     print(n*i)
#     i+=1
# print("loop end")
#--list print
# nums=[1,4,9,16,25]
# index=0
# while index < len(nums):
#     print(nums[index])
#     index +=1
# #----list 2 print
# Hero =["raees","Khan"]
# index=0
# while index < len(Hero):
#     print(Hero[index])
#     index+=1
# num= [1,2,3,4,5,6,7,8,2,9,10]
# i = 0
# x= 2
# while i < len(num):
#     if num[i] == x :
#         print("Founded at indx:", i)
#     else:
#        print("finding..")
#     i += 1
#--break and continue---
# i=1
# while i<=5:
#     print(i)
#     if i==3:
#         break
#     i+=1
# num=[1,2,3,4,5,6,7,8,9]
# idx=0
# x=7
# while idx<len(num):
#     if (num[idx]==x):
#       print("idx found at",idx)
#       break
#     else:
#          print("finding")
#          idx += 1
# print("loop end")
#continue
i=0
while i<=5:
    if(i==2):
       i+=1
       continue
    print(i)
    i+=1