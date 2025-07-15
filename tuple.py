# marks= (100,56,45)
# Name= ("Hemayat","Khan","Rehman")
# print(marks,Name)
# Fruits= ("Orange","Banana","Mango","Cheery")
# for fruit in Fruits:
#     print(fruit)
# ------------Dic---------------
# book = {
#     "title": "Python 101",
#     "author": "John",
#     "pages": 200
# }
# print(book)
# for Student in range(4):
#     Student= {
    
#     "Name":"Hemayat",
#     "FName":"Hidayat",
#     "Roll":"2430 0198",
#     "Degree":"Bs AI",
#     "GPA":3.5
# }
# print(Student)
# print('\n'.join(f"{k}: {v}" for k, v in {"Name": "Hemayat", "FName": "Hidayat", "Roll": "2430 0198", "Degree": "Bs AI", "GPA": 3.5}.items()))
# --------set Datatype-----------
# a= {1,2,3,4}
# b= {2,3,4,5}
# c={4,5,6,7}
# print(a|b|c)# union operation
# print(a&b&c)# intersection operation
# print(a-b-c)# difference operation
# print(a^b^c)# symmetric difference: it means that two sets has a unique value
# --------complex Datatype----------
# y= 2j
# print(y)
# x= 3 + 4j
# print("Real:",x.real)
# print("Imaginary:",x.imag)
# X= 3 + 5j
# Y= 4+ 10j
# print(X+Y)
# ---- Frozenset Datatype------------
# a = frozenset({1, 2, 3})
# b = frozenset({3, 4, 5})

# print(a | b)  # Union: frozenset({1, 2, 3, 4, 5})
# print(a & b)  # Intersection: frozenset({3})
# print(a - b)

# ------bool Datatype--------
# for _ in range(6):
#     Age = int(input("Enter your Age: "))
#     if Age >= 18:
#         print("Eligible (True)")
#     else:
#         print("Not Eligible (False)")
# ---- bytes datatype----
# text = "Python is fun"
# b = text.encode()
# print(b)
# print(b[0])

# text= "I am Hemayat"
# b= text.decode()
# empty = bytes()
# print(empty)         # Output: b''
# y= None
# print(type(y))
# b= bytearray([67,68])
# print(b)

# b.append[66]
# print(b)
import random

# num = random.randint(1, 100)
# print("Random number:", num)
# a= random.choice(1,10)
# print(a)
secret= random.randint(1,20)
attempt= 5
for _ in range(attempt):
    Guess=int(input("Enter your Number:"))
    if Guess== secret:
        print("You got the number")
        break
    elif Guess> secret:
        print("Too high")
    else:
        print("Too low")
        
        if attempt>5:
            print("your attempt ended")
            break