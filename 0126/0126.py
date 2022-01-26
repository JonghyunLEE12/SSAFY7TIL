# class Person:
    
#     def greeting(self):
#         print('안녕하세요' + self.name + '입니다.')


# jimin = Person()
# jimin.name = '지민'
# jimin.phone = '123456789'
# jimin.greeting()

# Jonghyun = Person()
# Jonghyun.name = '종현'
# Jonghyun.phone = '123456'
# Jonghyun.greeting()


# class Rectangle:    
#     def area(self):
#         return self.x * self.y

# r1 = Rectangle()
# r1.x = 100
# r1.y = 200
# print(r1.area())

# class Person:
#     def ead (self , *food):
#         print(f'{food}를 냠냠')

# class Person :
#     def test(self):
#         return print('test')

# p1 = Person()
# p1.test()


#생성자 메서드

# class Person :
#     def __init__(self , name , age):
#         #인스턴스 변수를 정의하기 위해 사용!
#         self.name = name
#         self.age = age

# p1 = Person('이종현','27')
# print(p1.name,p1.age)


# # 소멸자 메서드
# class Person:
#     def __init__(self):
#         print('안녕하세요')
#     def __del__(self):
#         print('bye bye')

# p100 = Person()
# del p100


# ##매직 메서드 활용
# class Person:
#     def __init__(self , name , age , height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def __lt__(self,other):
#         print(f'{self.name} : {self.age}살 / {other.name} : {other.age}살')
#         return self.age > other.age
    
#     def __len__(self):
#         return self.height
    
#     def __str__(self):
#         return f'<{self.name}> : {self.age}살'

# p1 = Person('종현',27,181)
# p2 = Person('수정',22,160)
# p1 > p2
# print(len(p1))
# p3 = Person('종수',5,130)
# print(p3)



# class Circle:
#     pi = 3.14
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return Circle.pi * self.r * self.r

# print(Circle.pi)
# c1= Circle(2)
# print(c1.area)

# c2= Circle(3)
# print(c2.area())

# class MyClass:
#     var ='Class 변수'
#     @classmethod
#     def class_method(cls):
#         print(cls.var)
#         return cls
# MyClass.class_method()
# MyClass


# #스태택 메서드
# class MyClass:
#     var ='Class 변수'
#     @staticmethod
#     def static_method():
#         return 'static'

# print(MyClass.static_method())

########################################################################################################
# 클래스 정의하기 ( = Type 정의하기 )
# class Person:
#     cnt = 0 #클래스 변수

#     #인스턴스 변수를 생성 하는 법
#     def __init__(self,name):
#         self.name  = name
#         #생성자 안에서 클래스 변수에 접근 한느 방법
#         Person.cnt +=1

# person_1 = Person('종현')
# print(person_1.name,person_1.cnt)
# person_2 = Person('수정')

# print(person_2.name,person_2.cnt)

#클래스 변수와 인스턴스 변수의 차이
'''
클래스로 만들어진 모든 인스턴스가 클래스 변수를 가지고 있음
인스턴스 변수는 만들어진 인스턴스에 하나하나 독립적인 변수

person_1 과 person_2 는 같은 cnt 를 공유하지만,
'종현'은 각각 가지고 있다.
'''

'''
파이썬은 인스턴스변수로 부터 인스턴스 생성 가능하다.
'''

# class Person:
#     cnt = 0 #클래스 변수

#     #인스턴스 변수를 생성 하는 법
#     def __init__(self,name):
#         self.name  = name
#         #생성자 안에서 클래스 변수에 접근 한느 방법
#         Person.cnt +=1
# person_1 = Person('종현')
# person_2 = Person('수정')

# person_1.cnt=3

# print(person_1.cnt)
# print(person_2)


# class MathUtility:
#     @staticmethod
#     def get_pi():
#         return 3.141592
#     @staticmethod
#     def get_e():
#         return 2
# print(MathUtility.get_pi())
# print(MathUtility.get_e())

# class PersonUtility:
#     @staticmethod
#     def get_phone_number(phone_number):
#         return phone_number[:2] + ')' + phone_number[2:]
# print(PersonUtility.get_phone_number('029627609'))


####################################
# 상속


# class Person:
#     population = 0

#     @classmethod
#     def add_population(cls):
#         cls.population +=1

# class Student(Person):
#     population= 0

# Person.add_population()
# print(Person.population)

# Student.add_population()
# print(Student.population)

#########################################
#다중 상속

# class A:
#     name ='A'

# class B:
#     name ='B'

# class C(A):
#     name  ='C'

# class D(B,C):
#     pass

# d = D()
# print(d.name)

#########################################
#캡슐화

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age 

#         def get_age(self):
#             return self._age

# p1 = Person('종현',23)
# print(p1._age)

##################################
#getter setter

class Person:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self , new_age):
        self._age = new_age - 10

p1 = Person(40)
print(p1.age)

