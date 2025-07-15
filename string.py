#--------string-----------
# three types of representation of string
# str= "Hi! its me "
# str1= 'I am the one'
# str2="""hello here i am"""
# print(str)
# print(str1)
# print(str2)
#-----operation on string-----
#---concatenation---
# str="Hemayat"# Method one
# str2="Khan"
# print(str+str2)
# str1="Sundas"
# str2="Ibrar"
# str3= str1 +" "+ str2
# print(str3)
#---length of string
# str="Hemayata"
# print(len(str))
# l=[1,2,3,4]
# print(len(l))
# print(type(l))
#-----indexing-----
# str="Alexandar"
# print(str[1])
# print(str[3])
# print(str[4])
#-----slicing----
# str="mardan"
# print(str[1:4])# strat from 1 and end on 3 index because 4 will b not include
# print(str[:4])#python will start it from 0 to 3
# print(str[4:])#start from the 4 index
# #--negative index---
# str1="Facebook"
# print(str1[-3:-1])
# print(str1[-5:len(str1)])
#--------Functions in string-------------#
#-----endswith func------#
# str= " I am genuis"
# print(str.endswith("uis"))
# print(str.endswith("are"))
# #------capitalize-----#
# str1=" here is the man"
# print(str1.strip().capitalize())# Here is the man
#-------strip--------#
#"its work is to remove space from\n
# begin and end"
# str=" Hemayat,  Khan! "
# print(str.strip())
#----replace funct-----#
# str="Hello,Hemayat"
# print(str.replace("Hello","Khan"))# [old,new]
#----Find funct----#
# str="Be ready i am coming to Mardan"
# print(str.find("m"))# it will show index from start output:12
#------upper funct-----#
# str=" Hemayata"
# print(str.upper())
# #-------lower funct-----#
# str1="Khan"
# print(str1.lower())
#-----count funct-----#
# str="I am your lover"
# print(str.count("o"))
# str1="I am coming Mardan be ready "
# print(str1.count("m"))
# Name=input("Enter your Name:")
# print(len(Name))
str="Hello Guys i have 7$"
print(str.count("$"))