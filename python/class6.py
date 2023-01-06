# class MyClass:
#     def add(self, a , b):
#         return a + b


# class Eclass(MyClass):
#     def square(self,c):
#         return c * c

# obj = Eclass()
# print(obj.add(4,5))
# print(obj.square(5))



class Person:
    def information(self,ID,name,department):
        return ID, name , department

# class Students(Person):
#     def student_information(self,roll):
#         return roll

# student_obj = Students()
# student = student_obj.information(1, 'Belal', 'CSE')
# student1 = student_obj.student_information(10)

# print(student,student1)

class Teacher(Person):
    def teacher_information(self,salary):
        return salary

# t_obj = Teacher()
# teacher = t_obj.information(5, 'Belal2', 'EEE')
# teacher1 = t_obj.teacher_information(12000)

# print(teacher,teacher1)


class Emplyee(Teacher):
    # def em_information(self, designation):
    #     return designation
    pass

em_obj = Emplyee()

print(em_obj.information(40, 'Akash', 'Eng'))

e_var = em_obj.information(40, 'Akash', 'Eng')
e_var1 = em_obj.teacher_information(30000)
# e_var3 = em_obj.em_information('officer')

print(e_var, e_var1)


#multiple inheritance

class Person:
    def information(self,ID,name,department):
        return ID, name , department

class Teacher:
    def teacher_information(self,salary):
        return salary

class Emplyee(Person,Teacher):
    # def em_information(self, designation):
    #     return designation
    def teacher_information(self,salary,designation):
        return salary,designation

em_obj = Emplyee()

e_var = em_obj.information(40, 'Akash', 'Eng')
e_var1 = em_obj.teacher_information(30000,'officer')
# e_var3 = em_obj.em_information('officer')

print(e_var, e_var1)






# class employee:
#     def emp_info(self,Id,name,department):
#         return Id, name, department

    
# class present_add:
#     def add1(self,section,block,road, house):
#         return section,block,road, house

# obj_pre_add = present_add()
    
# class permanent_add:
#     def add2(self,vill,thana,district):
#         return vill,thana,district
# obj_par_add = permanent_add()
    
# class all_class(employee,present_add, permanent_add):
#     pass

# obj1 = all_class()

# m_info = obj1.emp_info(100,'Aslam', 'Admin')
# m_preadd = obj1.add1(10, 'C', 14, 6)
# m_peradd = obj1.add2('Rasulpur', 'Nandail', 'Mymensingh')

# print(m_info, m_preadd, m_peradd)

# a='aslam'

# print (a.upper())

def uppercase_decorator(f):
    def change():
        func = f()
        make_uppercase = func.upper()  
        return make_uppercase
    return change

@uppercase_decorator
def say_hi():
    name = 'belal'
    return name

print(say_hi())

@uppercase_decorator
def say_hj():
    return 'hello hello there'

print(say_hj())


# def d_fuc(fun):
#     def wrapper():
#         print('#######')
#         fun()
#         fun()
#         fun()
#         print('@@@')
#     return wrapper

# @d_fuc
# def a_dec():
#     print('Hello')

# a_dec()