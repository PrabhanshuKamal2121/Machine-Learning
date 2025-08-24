# gender = str(input('enter you gender:')).lower()
# if gender =='male':
#     print(f'good morning{gender} sir')
# elif gender=='female':
#     print(f"good morning {gender} human")
# else:
#     print('does not exist')

# a = "prbahnashukamal2121@gmail.com"
# data=''
# for i in range(len(a)):
#     if a[i]=='@':
#         for j in range(i,len(a)):
#             data = data+a[j]
    

# print(data)


# a=str(input('word for pallidrome test:'))
# # b=""
# # for i in range(len(a)-1,-1,-1):
# #     b=b+a[i]
# # print(b)
# i=len(a)-1
# b=""
# while(i>-1):
#     b=b+a[i] 
#     i=i-1

# print(b)


# print 
# list = [1,2,2,5,3,4,5]
# # positive_number = []
# # negative_number = []
# # for i in list:
# #     if i<0:
# #         positive_number.append(i)
# #     elif i>0:
# #         negative_number.append(i)
# #     else:
# #         pass

# # print(positive_number)
# # print(negative_number)

# #mean of list elements
# sum=0
# num=0
# for i in list:
#     sum=sum+i
#     num=num+1

# mean  = sum/num
# print (f"the sum is {sum} and total numbers are {num} and their mean is {mean}")
# print(len(list))

# list = [1,2,2,5,3,4,5]
# greatest_number=[0]
# for i in range(0,len(list)-1):
#     if list[i]>greatest_number[0]:
#         greatest_number.insert(0,list[i])
#     pass

# print(greatest_number[0])


# Dic1 = {'name':'prabhanshu','rollNo':'2023UEE4670','section':2}
# Dic2 = {'maths_marks':90,'science_marks':80}

# for j in Dic2:
#     Dic1[j]=Dic2[j]

# for i in Dic1:
#     print(i,":",Dic1[i])

# try:
#     print(hello)
# except Exception as err:
#     print(err)


# class Factory:
#     def __init__(self,material,zips,pocket):
#         self.material=material
#         self.zips=zips
#         self.pocket = pocket

#     def shor(self):
#         print(f"list is {self.material},{self.zip},{self.pocket}")
        


# rebook = Factory("hello","yellow","dirtyfellow")

# print(rebook.material)

# class Animal:
#     name="lion"
#     def __init__(self,age):
#         self.age=age
    
#     @classmethod
#     def hello(cls):
#         print(f'this is good {cls.name} name')

# obj = Animal(5)

# obj.hello()

# class animal:
#     name1='hello'

# class human:
#     name2='yellow'

# class robot(animal,human):
#     name3='buffalo'
## inheritance ka order bhi badal jayega

# obj = robot
# print(obj.name1)

# class factory:
#     def __init__(self,material,zips):
#         self.material=material
#         self.zips=zips
    
# class bhopalfactory(factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color = color

# class mumbaifactory(bhopalfactory):
#     def __init__(self,material,zip,color,pocket):
#         super().__init__(material,zip,color)
#         self.pocket=pocket


# class encapsulation_Example:
#     def __init__(self,name,rollno,password):
#         self.name=name
#         self.rollno=rollno
#         self.__password=password

#     def password_Check(self):
#         print(f'this is your password - {self.__password}')

# password_test=encapsulation_Example('prabhanshu','2023UEE4670','Neveraccess')
# print(password_test.__password)
# # print(password_test._encapsulation_Example__password) not a good practice

# from abc import ABC,abstractmethod
# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass 

#     ## basically ek aise chiz jo must ho gayi hai ki obj meh uska hona must hai

# class square(abstract):
#     def __init__(self,side):
#         self.side=side
    
#     def perimeter(self):
#         pass

#     def area(self):
#         pass


#     #upar ke dono important hai dene jab abstract class method pass hua hai

# square_obj = square(5)

# class Money:
#     def __init__(self, amount):
#         self.amount = amount
    
#     def __add__(self, other):
#         return Money(self.amount + other.amount)
    
#     def __str__(self):
#         return f"${self.amount}"

# m1 = Money(50)
# m2 = Money(30)
# m3 = m1 + m2     # __add__ is called here
# print(m3)        # $80


# 1. __str__ → String Representation
# Called when you use str(object) or print(object).
# Purpose: To return a human-readable representation of your object.
# Should return a string (not print it).


# 2. __add__ → Overloading the + Operator
# Called when you use object1 + object2.
# Purpose: To define custom behavior for addition.
# Should return a new object (or appropriate type).