# from datetime import datetime as dt


# def time_display_decorator(origin_func):
#     def decorated():
#         print(dt.now())
#         origin_func()
#         print('------')
#     return decorated
# class TimeDisplay():
#     def __init__(self,origin_func):
#         self.origin_func = origin_func
#     def __call__(self):
#         print(dt.now())
#         self.origin_func()
#         print('--------')


# @time_display_decorator
# def test_a():
#     print('test_a')

# @TimeDisplay
# def test_b():
#     print('test_b')

# test_a()
# test_b()

##############################


# public , protected , private

# class Person:
#     def __init__(self,age):
#         self.__age = age
    
#     #getter 메소드 : 뭔가를 주는거
#     def get_age(self):
#         return self.__age
    
#     #setter 메소드 : 뭔가를 설정함
#     def set_age(self):
#         self.__age += 1

# tony = Person(27)
# # print(tony.__age)

# print(tony.get_age())

# tony.set_age()

# print(tony.get_age())

##############################

# class Person:
#     def __init__(self):
#         self.__age = None
#         self.__name = None
    
#     #매직 메소드
#     def __str__(self):
#         return f'나이는 {self.name}살 이구요, 이름은 {self.name} 입니다!'
    
#     #getter 메소드 : 뭔가를 주는거
#     def get_age(self):
#         return self.__age
    
#     #setter 메소드 : 뭔가를 설정,할당 함
#     def set_age(self,new_age):
#         self.__age = new_age

#     @property 
#     def name(self): #getter
#         return self.__name
#     @name.setter
#     def name(self, new_name): #setter
#         self.__name = new_name 

# jonghyun = Person()
# jonghyun.set_age(24)

# jonghyun.name = 'Jonghyun'
# print(jonghyun.name)

# jonghyun.name = 'JonghyunLEE'
# print(jonghyun.name)

# ##__str__ 메소드로 인해 가능
# print(jonghyun)


from datetime import datetime
now = datetime.now()

print(str(now))
print(repr(now))
